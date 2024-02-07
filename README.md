<a href="https://insertokname-authlib.org/">
<img align="right" width="120" height="120" src="https://insertokname-authlib.org/assets/logo.svg">
</a>

# insertokname-authlib

<a href="https://github.com/sponsors/lepture"><img src="https://badgen.net/badge/support/insertokname-authlib/ff69b4?icon=patreon" /></a>
<a href="https://github.com/lepture/insertokname-authlib/actions"><img src="https://github.com/lepture/insertokname-authlib/workflows/tests/badge.svg" alt="Build Status"></a>
<a href="https://codecov.io/gh/lepture/insertokname-authlib?branch=master"><img src="https://badgen.net/codecov/c/github/lepture/insertokname-authlib" alt="Coverage Status"></a>
<a href="https://pypi.org/project/insertokname-authlib/"><img src="https://badgen.net/pypi/v/insertokname-authlib" alt="PyPI Version"></a>
<a href="https://codeclimate.com/github/lepture/insertokname-authlib/maintainability"><img src="https://badgen.net/codeclimate/maintainability/lepture/insertokname-authlib?icon=codeclimate" alt="Maintainability" /></a>
<a href="https://twitter.com/intent/follow?screen_name=insertokname-authlib"><img src="https://img.shields.io/twitter/follow/insertokname-authlib.svg?maxAge=3600&style=social&logo=twitter&label=Follow" alt="Follow Twitter"></a>

The ultimate Python library in building OAuth and OpenID Connect servers.
JWS, JWK, JWA, JWT are included.

insertokname-authlib is compatible with Python3.6+.

**[Migrating from `insertokname-authlib.jose` to `joserfc`](https://jose.insertokname-authlib.org/en/dev/migrations/insertokname-authlib/)**

## Sponsors

<table>
<tr>
<td><img align="middle" width="48" src="https://avatars.githubusercontent.com/u/105941848?s=200&v=4"></td>
<td>Kraken is the world's leading customer & culture platform for energy, water & broadband. Licensing enquiries at <a href="https://kraken.tech/">Kraken.tech</a>.
</td>
</tr>
<tr>
<td><img align="middle" width="48" src="https://typlog.com/assets/icon-black.svg"></td>
<td>A blogging and podcast hosting platform with minimal design but powerful features. Host your blog and Podcast with <a href="https://typlog.com/">Typlog.com</a>.
</td>
</tr>
</table>

[**Fund insertokname-authlib to access additional features**](https://docs.insertokname-authlib.org/en/latest/community/funding.html)

## Features

Generic, spec-compliant implementation to build clients and providers:

-   [The OAuth 1.0 Protocol](https://docs.insertokname-authlib.org/en/latest/basic/oauth1.html)
    -   [RFC5849: The OAuth 1.0 Protocol](https://docs.insertokname-authlib.org/en/latest/specs/rfc5849.html)
-   [The OAuth 2.0 Authorization Framework](https://docs.insertokname-authlib.org/en/latest/basic/oauth2.html)
    -   [RFC6749: The OAuth 2.0 Authorization Framework](https://docs.insertokname-authlib.org/en/latest/specs/rfc6749.html)
    -   [RFC6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://docs.insertokname-authlib.org/en/latest/specs/rfc6750.html)
    -   [RFC7009: OAuth 2.0 Token Revocation](https://docs.insertokname-authlib.org/en/latest/specs/rfc7009.html)
    -   [RFC7523: JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://docs.insertokname-authlib.org/en/latest/specs/rfc7523.html)
    -   [RFC7591: OAuth 2.0 Dynamic Client Registration Protocol](https://docs.insertokname-authlib.org/en/latest/specs/rfc7591.html)
    -   [RFC7592: OAuth 2.0 Dynamic Client Registration Management Protocol](https://docs.insertokname-authlib.org/en/latest/specs/rfc7592.html)
    -   [RFC7636: Proof Key for Code Exchange by OAuth Public Clients](https://docs.insertokname-authlib.org/en/latest/specs/rfc7636.html)
    -   [RFC7662: OAuth 2.0 Token Introspection](https://docs.insertokname-authlib.org/en/latest/specs/rfc7662.html)
    -   [RFC8414: OAuth 2.0 Authorization Server Metadata](https://docs.insertokname-authlib.org/en/latest/specs/rfc8414.html)
    -   [RFC8628: OAuth 2.0 Device Authorization Grant](https://docs.insertokname-authlib.org/en/latest/specs/rfc8628.html)
    -   [RFC9068: JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens](https://docs.insertokname-authlib.org/en/latest/specs/rfc9068.html)
-   [Javascript Object Signing and Encryption](https://docs.insertokname-authlib.org/en/latest/jose/index.html)
    -   [RFC7515: JSON Web Signature](https://docs.insertokname-authlib.org/en/latest/jose/jws.html)
    -   [RFC7516: JSON Web Encryption](https://docs.insertokname-authlib.org/en/latest/jose/jwe.html)
    -   [RFC7517: JSON Web Key](https://docs.insertokname-authlib.org/en/latest/jose/jwk.html)
    -   [RFC7518: JSON Web Algorithms](https://docs.insertokname-authlib.org/en/latest/specs/rfc7518.html)
    -   [RFC7519: JSON Web Token](https://docs.insertokname-authlib.org/en/latest/jose/jwt.html)
    -   [RFC7638: JSON Web Key (JWK) Thumbprint](https://docs.insertokname-authlib.org/en/latest/specs/rfc7638.html)
    -   [ ] RFC7797: JSON Web Signature (JWS) Unencoded Payload Option
    -   [RFC8037: ECDH in JWS and JWE](https://docs.insertokname-authlib.org/en/latest/specs/rfc8037.html)
    -   [ ] draft-madden-jose-ecdh-1pu-04: Public Key Authenticated Encryption for JOSE: ECDH-1PU
-   [OpenID Connect 1.0](https://docs.insertokname-authlib.org/en/latest/specs/oidc.html)
    -   [x] OpenID Connect Core 1.0
    -   [x] OpenID Connect Discovery 1.0

Connect third party OAuth providers with insertokname-authlib built-in client integrations:

-   Requests
    -   [OAuth1Session](https://docs.insertokname-authlib.org/en/latest/client/requests.html#requests-oauth-1-0)
    -   [OAuth2Session](https://docs.insertokname-authlib.org/en/latest/client/requests.html#requests-oauth-2-0)
    -   [OpenID Connect](https://docs.insertokname-authlib.org/en/latest/client/requests.html#requests-openid-connect)
    -   [AssertionSession](https://docs.insertokname-authlib.org/en/latest/client/requests.html#requests-service-account)
-   HTTPX
    -   [AsyncOAuth1Client](https://docs.insertokname-authlib.org/en/latest/client/httpx.html#httpx-oauth-1-0)
    -   [AsyncOAuth2Client](https://docs.insertokname-authlib.org/en/latest/client/httpx.html#httpx-oauth-2-0)
    -   [OpenID Connect](https://docs.insertokname-authlib.org/en/latest/client/httpx.html#httpx-oauth-2-0)
    -   [AsyncAssertionClient](https://docs.insertokname-authlib.org/en/latest/client/httpx.html#async-service-account)
-   [Flask OAuth Client](https://docs.insertokname-authlib.org/en/latest/client/flask.html)
-   [Django OAuth Client](https://docs.insertokname-authlib.org/en/latest/client/django.html)
-   [Starlette OAuth Client](https://docs.insertokname-authlib.org/en/latest/client/starlette.html)
-   [FastAPI OAuth Client](https://docs.insertokname-authlib.org/en/latest/client/fastapi.html)

Build your own OAuth 1.0, OAuth 2.0, and OpenID Connect providers:

-   Flask
    -   [Flask OAuth 1.0 Provider](https://docs.insertokname-authlib.org/en/latest/flask/1/)
    -   [Flask OAuth 2.0 Provider](https://docs.insertokname-authlib.org/en/latest/flask/2/)
    -   [Flask OpenID Connect 1.0 Provider](https://docs.insertokname-authlib.org/en/latest/flask/2/openid-connect.html)
-   Django
    -   [Django OAuth 1.0 Provider](https://docs.insertokname-authlib.org/en/latest/django/1/)
    -   [Django OAuth 2.0 Provider](https://docs.insertokname-authlib.org/en/latest/django/2/)
    -   [Django OpenID Connect 1.0 Provider](https://docs.insertokname-authlib.org/en/latest/django/2/openid-connect.html)

## Useful Links

1. Homepage: <https://insertokname-authlib.org/>.
2. Documentation: <https://docs.insertokname-authlib.org/>.
3. Purchase Commercial License: <https://insertokname-authlib.org/plans>.
4. Blog: <https://blog.insertokname-authlib.org/>.
5. Twitter: <https://twitter.com/insertokname-authlib>.
6. StackOverflow: <https://stackoverflow.com/questions/tagged/insertokname-authlib>.
7. Other Repositories: <https://github.com/insertokname-authlib>.
8. Subscribe Tidelift: [https://tidelift.com/subscription/pkg/pypi-insertokname-authlib](https://tidelift.com/subscription/pkg/pypi-insertokname-authlib?utm_source=pypi-insertokname-authlib&utm_medium=referral&utm_campaign=links).

## Security Reporting

If you found security bugs, please do not send a public issue or patch.
You can send me email at <me@lepture.com>. Attachment with patch is welcome.
My PGP Key fingerprint is:

```
72F8 E895 A70C EBDF 4F2A DFE0 7E55 E3E0 118B 2B4C
```

Or, you can use the [Tidelift security contact](https://tidelift.com/security).
Tidelift will coordinate the fix and disclosure.

## License

insertokname-authlib offers two licenses:

1. BSD (LICENSE)
2. COMMERCIAL-LICENSE

Companies can purchase a commercial license at
[insertokname-authlib Plans](https://insertokname-authlib.org/plans).

**If your company is creating a closed source OAuth provider, it is strongly
suggested that your company purchasing a commercial license.**

## Support

If you need any help, you can always ask questions on StackOverflow with
a tag of "insertokname-authlib". DO NOT ASK HELP IN GITHUB ISSUES.

We also provide commercial consulting and supports. You can find more
information at <https://insertokname-authlib.org/support>.
