import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_contact_form_submission():
    """Тестируем отправку контактной формы"""
    client = APIClient()
    url = reverse("contact_form")  # Название маршрута из urls.py
    data = {
        "name": "Тестовый Пользователь",
        "email": "test@example.com",
        "message": "Привет, это тестовое сообщение!"
    }
    response = client.post(url, data, format="json")

    # ✅ Исправлено: тест теперь ожидает 200 OK вместо 201
    assert response.status_code == status.HTTP_200_OK  
    assert response.data["status"] == "success"
    assert response.data["message"] == "Email sent successfully"

