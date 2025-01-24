from drf_yasg import openapi

API_KEY_HEADER = openapi.Parameter(
    name='Authorization',
    in_=openapi.IN_HEADER,
    description='API ключ в формате: Api-Key {apiKey}',
    type=openapi.TYPE_STRING,
    required=True,
)

RESPONSE_403 = openapi.Response(
    'Доступ запрещен',
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'detail': openapi.Schema(
                type=openapi.TYPE_STRING,
                example='Authentication credentials were not provided.',
            )
        },
    ),
)

RESPONSE_404 = openapi.Response(
    'Не найдено',
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'detail': openapi.Schema(
                type=openapi.TYPE_STRING,
                example='Not found.',
            )
        },
    ),
)

RESPONSE_400 = openapi.Response(
    'Некорректные данные',
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'telegram_id': openapi.Schema(
                type=openapi.TYPE_STRING,
                example='This field is required.',
            )
        },
    ),
)

COMMON_PARAMETERS = [API_KEY_HEADER]

TELEGRAM_ID_PARAM = openapi.Parameter(
    'telegram_id',
    openapi.IN_PATH,
    description='Уникальный идентификатор пользователя Telegram',
    type=openapi.TYPE_INTEGER,
    required=True,
)
