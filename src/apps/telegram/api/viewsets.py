from typing import Any

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey

from apps.telegram.api.serializers import TelegramUserSerializer
from apps.telegram.models import TelegramUser
from apps.telegram.schemas import TelegramUserViewSetSwagger


class TelegramUserViewSet(viewsets.ModelViewSet):
    """ViewSet для модели TelegramUser."""

    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    permission_classes = [HasAPIKey]
    http_method_names = ['get', 'post']
    lookup_field = 'telegram_id'

    @TelegramUserViewSetSwagger.retrieve()
    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Получить пользователя по telegram_id."""
        return super().retrieve(request, *args, **kwargs)

    @TelegramUserViewSetSwagger.list()
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Получить список всех пользователей."""
        return super().list(request, *args, **kwargs)

    @TelegramUserViewSetSwagger.create()
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Создать нового пользователя."""
        return super().create(request, *args, **kwargs)
