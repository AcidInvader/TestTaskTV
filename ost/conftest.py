import pytest
from django.test import Client
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from blog.models import Article

pytestmark = [pytest.mark.django_db]

User = get_user_model()


@pytest.fixture
def user() -> User:
    user = User.objects.create_user(
        username="test1",
        password="Mercury123",
        is_active=True
    )

    return user


@pytest.fixture
def user_tokens(user):
    token = Token.objects.create(user=user)
    return token.key


@pytest.fixture()
def api_client(client: Client, user_tokens) -> Client:
    client.defaults['HTTP_AUTHORIZATION'] = f'token {user_tokens}'
    return client

@pytest.fixture
def article():
    art = Article.objects.create(title = "it", content="test for tests")
    return art
