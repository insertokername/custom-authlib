import os
from insertokname-authlib.integrations.django_oauth1 import (
    CacheAuthorizationServer,
)
from tests.django_helper import TestCase as _TestCase
from .models import Client, TokenCredential


class TestCase(_TestCase):
    def setUp(self):
        super().setUp()
        os.environ['insertokname-authlib_INSECURE_TRANSPORT'] = 'true'

    def tearDown(self):
        os.environ.pop('insertokname-authlib_INSECURE_TRANSPORT')
        super().tearDown()

    def create_server(self):
        return CacheAuthorizationServer(Client, TokenCredential)
