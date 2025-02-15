import os
from re import U
import sys
import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

# Добавляем backend в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture
def auth_client(db):
    """Создает пользователя и аутентифицированный API-клиент"""
    user = User.objects.create_user(username="testuser", password="password")
    client = APIClient()
    client.force_authenticate(user=user)
    return client
