import pytest
from django.urls import reverse
from rest_framework import status

from store.models import Book
from store.serializers import BooksSerializer


@pytest.fixture
def test_data():
    Book.objects.create(name="Book1", price=4000)


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.mark.django_db
class TestBooks:
    @pytest.mark.usefixtures("test_data")
    def test_get_books_list(self, api_client):
        url = reverse("book-list")
        excepted_data = BooksSerializer(Book.objects.all(), many=True).data
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == excepted_data
        assert response.data[0]["name"] == Book.objects.first().name
