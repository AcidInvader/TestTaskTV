import pytest
from rest_framework.reverse import reverse
from django.test import Client


def test_create_article(api_client: Client,):
    url = reverse("api:blog:article-create")
    data = {
        "title": "hakers",
        "content": "this is test content"
    }
    response = api_client.post(url, data)
    assert response.status_code == 201
