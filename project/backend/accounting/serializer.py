from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        required=True
    )

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        # Используем pop с дефолтом, чтобы избежать KeyError,
        # но затем выбрасываем ошибку, если пароль не указан.
        password = validated_data.pop('password', None)
        if not password:
            raise serializers.ValidationError({"password": "Это поле обязательно."})
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user




