import pytest
from django.contrib.auth import get_user_model
from accounting.models import CustomUser  # Импортируем модель

@pytest.mark.django_db
def test_create_user():
    """Проверяем, что пользователь создается корректно"""
    user = CustomUser.objects.create_user(username="testuser", password="password123")
    assert user.username == "testuser"
    assert user.check_password("password123")  # Проверяем, что пароль хэшируется

@pytest.mark.django_db
def test_create_superuser():
    """Проверяем, что суперпользователь создается корректно"""
    user = CustomUser.objects.create_superuser(username="admin", password="adminpass")
    assert user.is_superuser
    assert user.is_staff

@pytest.mark.django_db
def test_user_str():
    """Проверяем строковое представление пользователя"""
    user = CustomUser.objects.create_user(username="testuser", password="password123")
    assert str(user) == "testuser"  # Проверяем, что __str__ работает правильно
