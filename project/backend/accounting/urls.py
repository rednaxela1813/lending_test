from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, AccountingListView  # Убедись, что импорт правильный

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),  # Это просто подключение роутера
    path("list/", AccountingListView.as_view(), name="accounting_list"),  # Вот тут name
]
