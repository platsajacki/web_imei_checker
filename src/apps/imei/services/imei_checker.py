from dataclasses import dataclass

from rest_framework import status
from rest_framework.response import Response

import requests

from apps.imei.api.serializers import DeviceSerializer
from core.services import BaseService
from core.settings import BASE_URL_IMEI_CHECK, IMEI_CHECK_TOKEN, main_loger


@dataclass
class IMEIChecker(BaseService):
    """
    Сервис для проверки устройства по IMEI или серийному номеру.

    Attributes:
        serializer (DeviceSerializer): Сериализатор для валидации входных данных.
    """

    serializer: DeviceSerializer

    def fetch_data(self, device_id: str) -> dict:
        """
        Отправляет запрос к внешнему API для получения информации об устройстве.

        Args:
            device_id (str): Идентификатор устройства (IMEI или серийный номер).

        Returns:
            dict: JSON-ответ с данными об устройстве или сообщением об ошибке.
        """
        url = f'{BASE_URL_IMEI_CHECK}checks'
        response = requests.post(
            url, json={'deviceId': device_id, 'serviceId': 1}, headers={'Authorization': f'Bearer {IMEI_CHECK_TOKEN}'}
        )
        data = response.json()
        if response.status_code != status.HTTP_201_CREATED or not isinstance(data, dict):
            main_loger.error('%s returned a response with status %d\nResponse: %s' % (url, response.status_code, data))
            return (
                {'data': 'Error. Please contact the administrator or try again later.'},
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return data, status.HTTP_200_OK

    def act(self) -> Response:
        """
        Выполняет валидацию данных и отправляет запрос к сервису IMEI.

        Returns:
            Response: JSON-ответ с результатами проверки устройства.
        """
        if self.serializer.is_valid():
            device_id = self.serializer.validated_data['device_id']
            device_info, status_code = self.fetch_data(device_id)
            return Response(device_info, status=status_code)
        return Response(self.serializer.errors, status=status.HTTP_400_BAD_REQUEST)
