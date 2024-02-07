from flask import json
from insertokname-authlib.common.urls import urlparse, url_decode
from insertokname-authlib.jose import jwt
from insertokname-authlib.oidc.core import HybridIDToken
from insertokname-authlib.oidc.core.grants import (
    OpenIDCode as _OpenIDCode,
    OpenIDHybridGrant as _OpenIDHybridGrant,
)
from insertokname-authlib.oauth2.rfc6749.grants import (
    AuthorizationCodeGrant as _AuthorizationCodeGrant,
)
from .models import db, User, Client, exists_nonce
from .models import CodeGrantMixin, save_authorization_code
from .oauth2_server import TestCase
from .oauth2_server import create_authorization_server

JWT_CONFIG = {'iss': 'insertokname-authlib', 'key': 'secret', 'alg': 'HS256', 'exp': 3600}


class AuthorizationCodeGrant(CodeGrantMixin, _AuthorizationCodeGrant):
    def save_authorization_code(self, code, request):
        return save_authorization_code(code, request)


class OpenIDCode(_OpenIDCode):
    def get_jwt_config(self, grant):
        return dict(JWT_CONFIG)

    def exists_nonce(self, nonce, request):
        return exists_nonce(nonce, request)

    def generate_user_info(self, user, scopes):
        return user.generate_user_info(scopes)


class OpenIDHybridGrant(_OpenIDHybridGrant):
    def save_authorization_code(self, code, request):
        return save_authorization_code(code, request)

    def get_jwt_config(self):
        return dict(JWT_CONFIG)

    def exists_nonce(self, nonce, request):
        return exists_nonce(nonce, request)

    def generate_user_info(self, user, scopes):
        return user.generate_user_info(scopes)


class OpenIDCodeTest(TestCase):
    def prepare_data(self):
        server = create_authorization_server(self.app)
        server.register_grant(OpenIDHybridGrant)
        server.register_grant(AuthorizationCodeGrant, [OpenIDCode()])

        user = User(username='foo')
        db.session.add(user)
        db.session.commit()

        client = Client(
            user_id=user.id,
            client_id='hybrid-client',
            client_secret='hybrid-secret',
        )
        client.set_client_metadata({
            'redirect_uris': ['https://a.b'],
            'scope': 'openid profile address',
            'response_types': ['code id_token', 'code token', 'code id_token token'],
            'grant_types': ['authorization_code'],
        })
        db.session.add(client)
        db.session.commit()

    def validate_claims(self, id_token, params):
        claims = jwt.decode(
            id_token, 'secret',
            claims_cls=HybridIDToken,
            claims_params=params
        )
        claims.validate()

    def test_invalid_client_id(self):
        self.prepare_data()
        rv = self.client.post('/oauth/authorize', data={
            'response_type': 'code token',
            'state': 'bar',
            'nonce': 'abc',
            'scope': 'openid profile',
            'redirect_uri': 'https://a.b',
            'user_id': '1',
        })
        resp = json.loads(rv.data)
        self.assertEqual(resp['error'], 'invalid_client')

        rv = self.client.post('/oauth/authorize', data={
            'client_id': 'invalid-client',
            'response_type': 'code token',
            'state': 'bar',
            'nonce': 'abc',
            'scope': 'openid profile',
            'redirect_uri': 'https://a.b',
            'user_id': '1',
        })
        resp = json.loads(rv.data)
        self.assertEqual(resp['error'], 'invalid_client')

    def test_require_nonce(self):
        self.prepare_data()
        rv = self.client.post('/oauth/authorize', data={
            'client_id': 'hybrid-client',
            'response_type': 'code token',
            'scope': 'openid profile',
            'state': 'bar',
            'redirect_uri': 'https://a.b',
            'user_id': '1'
        })
        self.assertIn('error=invalid_request', rv.location)
        self.assertIn('nonce', rv.location)

    def test_invalid_response_type(self):
        self.prepare_data()
        rv = self.client.post('/oauth/authorize', data={
            'client_id': 'hybrid-client',
            'response_type': 'code id_token invalid',
            'state': 'bar',
            'nonce': 'abc',
            'scope': 'profile',
            'redirect_uri': 'https://a.b',
            'user_id': '1',
        })
        resp = json.loads(rv.data)
        self.assertEqual(resp['error'], 'unsupported_response_type')

    def test_invalid_scope(self):
        self.prepare_data()
        rv = self.client.post('/oauth/authorize', data={
            'client_id': 'hybrid-client',
            'response_type': 'code id_token',
            'state': 'bar',
            'nonce': 'abc',
            'scope': 'profile',
            'redirect_uri': 'https://a.b',
            'user_id': '1',
        })
        self.assertIn('error=invalid_scope', rv.location)

    def test_access_denied(self):
        self.prepare_data()
        rv = self.client.post('/oauth/authorize', data={
            'client_id': 'hybrid-client',
            'response_type': 'code token',
            'state': 'bar',
            'nonce': 'abc',
            'scope': 'openid profile',
            'redirect_uri': 'https://a.b',
        })
        self.assertIn('error=access_denied', rv.location)

    def test_code_access_token(self):
        self.prepare_data()
        rv = self.client.post('/oauth/authorize', data={
            'client_id': 'hybrid-client',
            'response_type': 'code token',
            'state': 'bar',
            'nonce': 'abc',
            'scope': 'openid profile',
            'redirect_uri': 'https://a.b',
            'user_id': '1',
        })
        self.assertIn('code=', rv.location)
        self.assertIn('access_token=', rv.location)
        self.assertNotIn('id_token=', rv.location)

        params = dict(url_decode(urlparse.urlparse(rv.location).fragment))
        self.assertEqual(params['state'], 'bar')

        code = params['code']
        headers = self.create_basic_header('hybrid-client', 'hybrid-secret')
        rv = self.client.post('/oauth/token', data={
            'grant_type': 'authorization_code',
            'redirect_uri': 'https://a.b',
            'code': code,
        }, headers=headers)
        resp = json.loads(rv.data)
        self.assertIn('access_token', resp)
        self.assertIn('id_token', resp)

    def test_code_id_token(self):
        self.prepare_data()
        rv = self.client.post('/oauth/authorize', data={
            'client_id': 'hybrid-client',
            'response_type': 'code id_token',
            'state': 'bar',
            'nonce': 'abc',
            'scope': 'openid profile',
            'redirect_uri': 'https://a.b',
            'user_id': '1',
        })
        self.assertIn('code=', rv.location)
        self.assertIn('id_token=', rv.location)
        self.assertNotIn('access_token=', rv.location)

        params = dict(url_decode(urlparse.urlparse(rv.location).fragment))
        self.assertEqual(params['state'], 'bar')

        params['nonce'] = 'abc'
        params['client_id'] = 'hybrid-client'
        self.validate_claims(params['id_token'], params)

        code = params['code']
        headers = self.create_basic_header('hybrid-client', 'hybrid-secret')
        rv = self.client.post('/oauth/token', data={
            'grant_type': 'authorization_code',
            'redirect_uri': 'https://a.b',
            'code': code,
        }, headers=headers)
        resp = json.loads(rv.data)
        self.assertIn('access_token', resp)
        self.assertIn('id_token', resp)

    def test_code_id_token_access_token(self):
        self.prepare_data()
        rv = self.client.post('/oauth/authorize', data={
            'client_id': 'hybrid-client',
            'response_type': 'code id_token token',
            'state': 'bar',
            'nonce': 'abc',
            'scope': 'openid profile',
            'redirect_uri': 'https://a.b',
            'user_id': '1',
        })
        self.assertIn('code=', rv.location)
        self.assertIn('id_token=', rv.location)
        self.assertIn('access_token=', rv.location)

        params = dict(url_decode(urlparse.urlparse(rv.location).fragment))
        self.assertEqual(params['state'], 'bar')
        self.validate_claims(params['id_token'], params)

        code = params['code']
        headers = self.create_basic_header('hybrid-client', 'hybrid-secret')
        rv = self.client.post('/oauth/token', data={
            'grant_type': 'authorization_code',
            'redirect_uri': 'https://a.b',
            'code': code,
        }, headers=headers)
        resp = json.loads(rv.data)
        self.assertIn('access_token', resp)
        self.assertIn('id_token', resp)

    def test_response_mode_query(self):
        self.prepare_data()
        rv = self.client.post('/oauth/authorize', data={
            'client_id': 'hybrid-client',
            'response_type': 'code id_token token',
            'response_mode': 'query',
            'state': 'bar',
            'nonce': 'abc',
            'scope': 'openid profile',
            'redirect_uri': 'https://a.b',
            'user_id': '1',
        })
        self.assertIn('code=', rv.location)
        self.assertIn('id_token=', rv.location)
        self.assertIn('access_token=', rv.location)

        params = dict(url_decode(urlparse.urlparse(rv.location).query))
        self.assertEqual(params['state'], 'bar')

    def test_response_mode_form_post(self):
        self.prepare_data()
        rv = self.client.post('/oauth/authorize', data={
            'client_id': 'hybrid-client',
            'response_type': 'code id_token token',
            'response_mode': 'form_post',
            'state': 'bar',
            'nonce': 'abc',
            'scope': 'openid profile',
            'redirect_uri': 'https://a.b',
            'user_id': '1',
        })
        self.assertIn(b'name="code"', rv.data)
        self.assertIn(b'name="id_token"', rv.data)
        self.assertIn(b'name="access_token"', rv.data)
