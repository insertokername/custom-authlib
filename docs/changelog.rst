Changelog
=========

.. meta::
    :description: The full list of changes between each insertokname-authlib release.

Here you can see the full list of changes between each insertokname-authlib release.

Version 1.3.0
-------------

**Released on Dec 17, 2023**

- Restore ``AuthorizationServer.create_authorization_response`` behavior, via :PR:`558`
- Include ``leeway`` in ``validate_iat()`` for JWT, via :PR:`565`
- Fix ``encode_client_secret_basic``, via :PR:`594`
- Use single key in JWK if JWS does not specify ``kid``, via :PR:`596`
- Fix error when RFC9068 JWS has no scope field, via :PR:`598`
- Get werkzeug version using importlib, via :PR:`591`

**New features**:

- RFC9068 implementation, via :PR:`586`, by @azmeuk.

**Breaking changes**:

- End support for python 3.7

Version 1.2.1
-------------

**Released on Jun 25, 2023**

- Apply headers in ``ClientSecretJWT.sign`` method, via :PR:`552`
- Allow falsy but non-None grant uri params, via :PR:`544`
- Fixed ``authorize_redirect`` for Starlette v0.26.0, via :PR:`533`
- Removed ``has_client_secret`` method and documentation, via :PR:`513`
- Removed ``request_invalid`` and ``token_revoked`` remaining occurences
  and documentation. :PR:`514`
- Fixed RFC7591 ``grant_types`` and ``response_types`` default values, via :PR:`509`.
- Add support for python 3.12, via :PR:`590`.

Version 1.2.0
-------------

**Released on Dec 6, 2022**

- Not passing ``request.body`` to ``ResourceProtector``, via :issue:`485`.
- Use ``flask.g`` instead of ``_app_ctx_stack``, via :issue:`482`.
- Add ``headers`` parameter back to ``ClientSecretJWT``, via :issue:`457`.
- Always passing ``realm`` parameter in OAuth 1 clients, via :issue:`339`.
- Implemented RFC7592 Dynamic Client Registration Management Protocol, via :PR:`505`.
- Add ``default_timeout`` for requests ``OAuth2Session`` and ``AssertionSession``.
- Deprecate ``jwk.loads`` and ``jwk.dumps``

Version 1.1.0
-------------

**Released on Sep 13, 2022**

This release contains breaking changes and security fixes.

- Allow to pass ``claims_options`` to Framework OpenID Connect clients, via :PR:`446`.
- Fix ``.stream`` with context for HTTPX OAuth clients, via :PR:`465`.
- Fix Starlette OAuth client for cache store, via :PR:`478`.

**Breaking changes**:

- Raise ``InvalidGrantError`` for invalid code, redirect_uri and no user errors in OAuth
  2.0 server.
- The default ``insertokname-authlib.jose.jwt`` would only work with JSON Web Signature algorithms, if
  you would like to use JWT with JWE algorithms, please pass the algorithms parameter::

      jwt = JsonWebToken(['A128KW', 'A128GCM', 'DEF'])

**Security fixes**: CVE-2022-39175 and CVE-2022-39174, both related to JOSE.

Version 1.0.1
-------------

**Released on Apr 6, 2022**

- Fix authenticate_none method, via :issue:`438`.
- Allow to pass in alternative signing algorithm to RFC7523 authentication methods via :PR:`447`.
- Fix ``missing_token`` for Flask OAuth client, via :issue:`448`.
- Allow ``openid`` in any place of the scope, via :issue:`449`.
- Security fix for validating essential value on blank value in JWT, via :issue:`445`.


Version 1.0.0
-------------

**Released on Mar 15, 2022.**

We have dropped support for Python 2 in this release. We have removed
built-in SQLAlchemy integration.

**OAuth Client Changes:**

The whole framework client integrations have been restructured, if you are
using the client properly, e.g. ``oauth.register(...)``, it would work as
before.

**OAuth Provider Changes:**

In Flask OAuth 2.0 provider, we have removed the deprecated
``OAUTH2_JWT_XXX`` configuration, instead, developers should define
`.get_jwt_config` on OpenID extensions and grant types.

**SQLAlchemy** integrations has been removed from insertokname-authlib. Developers
should define the database by themselves.

**JOSE Changes**

- ``JWS`` has been renamed to ``JsonWebSignature``
- ``JWE`` has been renamed to ``JsonWebEncryption``
- ``JWK`` has been renamed to ``JsonWebKey``
- ``JWT`` has been renamed to ``JsonWebToken``

The "Key" model has been re-designed, checkout the :ref:`jwk_guide` for updates.

Added ``ES256K`` algorithm for JWS and JWT.

**Breaking Changes**: find how to solve the deprecate issues via https://git.io/JkY4f


Old Versions
------------

Find old changelog at https://github.com/lepture/insertokname-authlib/releases

- Version 0.15.5: Released on Oct 18, 2021
- Version 0.15.4: Released on Jul 17, 2021
- Version 0.15.3: Released on Jan 15, 2021
- Version 0.15.2: Released on Oct 18, 2020
- Version 0.15.1: Released on Oct 14, 2020
- Version 0.15.0: Released on Oct 10, 2020
- Version 0.14.3: Released on May 18, 2020
- Version 0.14.2: Released on May 6, 2020
- Version 0.14.1: Released on Feb 12, 2020
- Version 0.14.0: Released on Feb 11, 2020
- Version 0.13.0: Released on Nov 11, 2019
- Version 0.12.0: Released on Sep 3, 2019
- Version 0.11.0: Released on Apr 6, 2019
- Version 0.10.0: Released on Oct 12, 2018
- Version 0.9.0: Released on Aug 12, 2018
- Version 0.8.0: Released on Jun 17, 2018
- Version 0.7.0: Released on Apr 28, 2018
- Version 0.6.0: Released on Mar 20, 2018
- Version 0.5.1: Released on Feb 11, 2018
- Version 0.5.0: Released on Feb 11, 2018
- Version 0.4.1: Released on Feb 2, 2018
- Version 0.4.0: Released on Jan 31, 2018
- Version 0.3.0: Released on Dec 24, 2017
- Version 0.2.1: Released on Dec 6, 2017
- Version 0.2.0: Released on Nov 25, 2017
- Version 0.1.0: Released on Nov 18, 2017
