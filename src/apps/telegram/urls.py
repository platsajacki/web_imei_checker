from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.telegram.api.viewsets import TelegramUserViewSet

router = DefaultRouter()
router.register(r'telegram-users', TelegramUserViewSet, basename='telegram-user')

app_name = 'telegram-users'

urlpatterns = [
    path('', include(router.urls)),
]
