import pytest
from rest_framework.reverse import reverse
from django.test import Client
from blog.models import Article
pytestmark = [pytest.mark.django_db]


def test_article_create(client: Client):
    url = reverse("api:blog:article-create")
    data = {
        "title": "hakers",
        "content": "this is test content"
    }
    response = client.post(url, data)
    created_article = Article.objects.last()
    assert response.status_code == 201
    assert created_article.title == "hakers"
    assert created_article.content == "this is test content"


def test_article_list(api_client: Client):
    url = reverse("api:blog:article-list")
    print(f"Request Headers: {api_client.defaults}")
    response = api_client.get(url)
    print(f"{response.json=}")
    assert response.status_code == 200


def test_comment_create(client: Client, user, article):
    url = reverse("api:blog:comment-create")
    data = {
        "author": user.id,
        "content": "This is the test for second article",
        "article": article.id
    }
    response = client.post(url, data)
    assert response.status_code == 201


def test_comments_article(api_client: Client):
    url = reverse("api:blog:comments-list")
    response = api_client.get(url)
    assert response.status_code == 200

