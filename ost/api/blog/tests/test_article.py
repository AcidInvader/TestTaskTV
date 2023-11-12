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


def test_article_list(client: Client):
    url = reverse("api:blog:article-list")
    response = client.get(url)
    print(f"{response.json=}")



def test_comment_create(client: Client):
    pass


def test_comments_article(client: Client):
    pass
