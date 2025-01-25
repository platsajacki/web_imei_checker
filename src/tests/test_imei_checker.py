from pytest_mock import MockType

from rest_framework import status

from apps.imei.api.serializers import DeviceSerializer
from apps.imei.services.imei_checker import IMEIChecker


class TestIMEIChecker:
    def test_invalide_device_id(self, mock_fetch_imei_data: MockType) -> None:
        data = {'device_id': 'device_id'}
        serializer = DeviceSerializer(data=data)
        response = IMEIChecker(serializer)()
        assert mock_fetch_imei_data.call_count == 0
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == serializer.errors

    def test_valide_device_id(self, mock_fetch_imei_data: MockType) -> None:
        data = {'device_id': '123456789012345'}
        serializer = DeviceSerializer(data=data)
        response = IMEIChecker(serializer)()
        assert mock_fetch_imei_data.call_count == 1
        assert response.status_code == status.HTTP_200_OK
        assert response.data == mock_fetch_imei_data.return_value.json()

    def test_valide_error_fetch_data(self, mock_fetch_imei_data: MockType) -> None:
        data = {'device_id': '123456789012345'}
        mock_fetch_imei_data.return_value.status_code = status.HTTP_401_UNAUTHORIZED
        serializer = DeviceSerializer(data=data)
        response = IMEIChecker(serializer)()
        assert mock_fetch_imei_data.call_count == 1
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.data == {'data': 'Error. Please contact the administrator or try again later.'}
