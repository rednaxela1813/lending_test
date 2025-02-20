import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse, get_resolver
from tests.conftest import auth_client  # Принудительный импорт фикстуры


def test_list_all_urls():
    """Выводит все зарегистрированные эндпоинты Django."""
    urlpatterns = get_resolver().url_patterns
    urls = []

    for pattern in urlpatterns:
        if hasattr(pattern, "pattern"):  # Проверяем, есть ли у паттерна `pattern`
            urls.append(str(pattern.pattern))

    print("\nВсе зарегистрированные маршруты Django:")
    if not urls:
        print("⚠️  Нет зарегистрированных маршрутов!")
    for url in urls:
        print(url)

    # Проверяем, что хотя бы один маршрут существует
    assert len(urls) > 0, "❌ В проекте нет зарегистрированных URL-маршрутов!"


@pytest.mark.django_db
def test_api_health_check(auth_client):
    """ Проверяет, доступен ли API """
    url = reverse("accounting_list")
    response = auth_client.get(url)  # Используем аутентифицированный клиент
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_user_detail(auth_client, django_user_model):
    """Тестируем получение конкретного пользователя"""
    user = django_user_model.objects.get(username="testuser")
    url = reverse("user-detail", kwargs={"pk": user.id})
    response = auth_client.get(url)
    assert response.status_code == 200
    assert response.data["username"] == user.username


@pytest.mark.django_db
class TestUserAPI:
    """Тестируем эндпоинты работы с пользователями"""

    def test_create_user(self, auth_client, django_user_model):
        url = reverse("user-list")
        data = {
            "username": "newuser",
            "password": "testpassword123",
        }
        response = auth_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert django_user_model.objects.filter(username="newuser").exists()

    def test_get_user_list(self, auth_client):
        url = reverse("user-list")
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list)

    def test_get_user_detail(self, auth_client, django_user_model):
        user = django_user_model.objects.get(username="testuser")
        url = reverse("user-detail", kwargs={"pk": user.id})
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["username"] == "testuser"

    def test_update_user(self, auth_client, django_user_model):
        user = django_user_model.objects.create_user(username="updatableuser", password="password")
        url = reverse("user-detail", kwargs={"pk": user.id})
        data = {"username": "updateduser"}
        response = auth_client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        user.refresh_from_db()
        assert user.username == "updateduser"

    def test_delete_user(self, auth_client, django_user_model):
        user = django_user_model.objects.create_user(username="deletableuser", password="password")
        url = reverse("user-detail", kwargs={"pk": user.id})
        response = auth_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not django_user_model.objects.filter(id=user.id).exists()
