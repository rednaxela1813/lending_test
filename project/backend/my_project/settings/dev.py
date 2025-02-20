from .base import *
import environ
import os

DEBUG = True

# Инициализация django-environ
env = environ.Env()

# Путь к .env.dev файлу (предполагаем, что он лежит в корне backend)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, ".env.dev"))

# Настройки почты
EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = env("EMAIL_HOST", default="localhost")
EMAIL_PORT = env("EMAIL_PORT", default=25)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=False)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="webmaster@localhost")

# Разрешаем доступ к Debug Toolbar только из локального хоста
INTERNAL_IPS = ["127.0.0.1"]

CORS_ALLOW_ALL_ORIGINS = True

# Если используешь конкретные домены:
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost",
]
