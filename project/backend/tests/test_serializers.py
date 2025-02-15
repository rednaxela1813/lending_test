import pytest
from accounting.serializer import UserSerializer
from accounting.models import CustomUser

@pytest.mark.django_db
def test_user_serializer_valid_data():
    """ Проверяем, что сериализатор принимает корректные данные """
    valid_data = {
        "username": "testuser",
        "password": "password123",
    }
    serializer = UserSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data["username"] == "testuser"

@pytest.mark.django_db
def test_user_serializer_invalid_data():
    """ Проверяем, что сериализатор отбраковывает некорректные данные """
    invalid_data = {
        "username": "",  # Имя пользователя не может быть пустым
        "password": "short",  # Пароль слишком короткий (менее 8 символов)
    }
    serializer = UserSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert "username" in serializer.errors
    assert "password" in serializer.errors  # Теперь ошибка пароля должна появиться


@pytest.mark.django_db
def test_user_serializer_serialization():
    """ Проверяем, что сериализатор корректно сериализует объект """
    user = CustomUser.objects.create_user(username="serialized_user", password="password123")
    serializer = UserSerializer(user)
    data = serializer.data
    assert data["username"] == "serialized_user"

