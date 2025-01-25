from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from core.schemas import COMMON_PARAMETERS, RESPONSE_400, RESPONSE_403

IMEI_RESPONSE_200 = openapi.Response(
    'Успешный ответ с информацией об устройстве',
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'data': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_STRING, example='a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'),
                    'type': openapi.Schema(type=openapi.TYPE_STRING, example='api'),
                    'status': openapi.Schema(type=openapi.TYPE_STRING, example='successful'),
                    'amount': openapi.Schema(type=openapi.TYPE_STRING, example='0.14'),
                    'deviceId': openapi.Schema(type=openapi.TYPE_STRING, example='123456789012345'),
                    'processedAt': openapi.Schema(type=openapi.TYPE_INTEGER, example=41241252112),
                    'service': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                            'title': openapi.Schema(type=openapi.TYPE_STRING, example='Apple Basic Info'),
                        },
                    ),
                    'properties': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        additionalProperties=openapi.Schema(type=openapi.TYPE_OBJECT),
                        example={
                            'deviceName': 'iPhone 11 Pro',
                            'image': 'https://sources.imeicheck.net/image.jpg',
                            'imei': '123456789012345',
                            'simLock': True,
                            'warrantyStatus': 'AppleCare Protection Plan',
                            'network': 'Global',
                        },
                    ),
                },
            ),
        },
    ),
)

IMEI_RESPONSE_500 = openapi.Response(
    description='Ошибка сервера или некорректный запрос',
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'data': openapi.Schema(
                type=openapi.TYPE_STRING,
                example='Error. Please contact the administrator or try again later.',
            ),
        },
    ),
)


class IMEIViewSwagger:
    """Класс для описания документации метода post в IMEIView."""

    @staticmethod
    def post():
        return swagger_auto_schema(
            operation_description='Проверка устройства по IMEI или серийному номеру',
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                required=['device_id'],
                properties={
                    'device_id': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='Уникальный идентификатор устройства (IMEI или серийный номер)',
                        example='356735111052198',
                    ),
                },
            ),
            manual_parameters=COMMON_PARAMETERS,
            responses={
                status.HTTP_200_OK: IMEI_RESPONSE_200,
                status.HTTP_400_BAD_REQUEST: RESPONSE_400,
                status.HTTP_403_FORBIDDEN: RESPONSE_403,
                status.HTTP_500_INTERNAL_SERVER_ERROR: IMEI_RESPONSE_500,
            },
        )
