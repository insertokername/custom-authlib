import os
import base64
from insertokname-authlib.common.encoding import to_bytes, to_unicode
from insertokname-authlib.integrations.django_oauth2 import AuthorizationServer
from tests.django_helper import TestCase as _TestCase
from .models import Client, OAuth2Token


class TestCase(_TestCase):
    def setUp(self):
        super().setUp()
        os.environ['insertokname-authlib_INSECURE_TRANSPORT'] = 'true'

    def tearDown(self):
        super().tearDown()
        os.environ.pop('insertokname-authlib_INSECURE_TRANSPORT')

    def create_server(self):
        return AuthorizationServer(Client, OAuth2Token)

    def create_basic_auth(self, username, password):
        text = f'{username}:{password}'
        auth = to_unicode(base64.b64encode(to_bytes(text)))
        return 'Basic ' + auth
