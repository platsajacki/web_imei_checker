from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.telegram.api.serializers import TelegramUserSerializer
from core.schemas import COMMON_PARAMETERS, RESPONSE_400, RESPONSE_403, RESPONSE_404, TELEGRAM_ID_PARAM


class TelegramUserViewSetSwagger:
    """Класс для описания документации методов TelegramUserViewSet."""

    @staticmethod
    def retrieve():
        return swagger_auto_schema(
            operation_description='Получение пользователя по telegram_id',
            manual_parameters=COMMON_PARAMETERS + [TELEGRAM_ID_PARAM],
            responses={
                status.HTTP_200_OK: TelegramUserSerializer(),
                status.HTTP_403_FORBIDDEN: RESPONSE_403,
                status.HTTP_404_NOT_FOUND: RESPONSE_404,
            },
        )

    @staticmethod
    def list():
        return swagger_auto_schema(
            operation_description='Получение списка всех пользователей Telegram',
            manual_parameters=COMMON_PARAMETERS,
            responses={
                status.HTTP_200_OK: TelegramUserSerializer(many=True),
                status.HTTP_403_FORBIDDEN: RESPONSE_403,
            },
        )

    @staticmethod
    def create():
        return swagger_auto_schema(
            operation_description='Создание нового пользователя Telegram',
            request_body=TelegramUserSerializer,
            manual_parameters=COMMON_PARAMETERS,
            responses={
                status.HTTP_201_CREATED: TelegramUserSerializer(),
                status.HTTP_400_BAD_REQUEST: RESPONSE_400,
                status.HTTP_403_FORBIDDEN: RESPONSE_403,
            },
        )
