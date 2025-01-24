import pytest
from pytest_mock import MockType

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class TestAvailabilityViewSet:
    @pytest.mark.parametrize(
        'method, url, data',
        [
            (
                'get',
                reverse('telegram-users:telegram-user-list'),
                None,
            ),
            (
                'post',
                reverse('telegram-users:telegram-user-list'),
                {'telegram_id': 123456789, 'username': 'test_user', 'name': 'Test', 'surname': 'User'},
            ),
            (
                'get',
                reverse('telegram-users:telegram-user-detail', kwargs={'telegram_id': 202022}),
                None,
            ),
            (
                'post',
                reverse('imei:check-imei'),
                {'telegram_id': 123456789, 'username': 'test_user', 'name': 'Test', 'surname': 'User'},
            ),
        ],
    )
    def test_not_availability_viewset(
        self, api_client: APIClient, method: str, url: str, data: dict | None, mock_fetch_imei_data: MockType
    ):
        response = getattr(api_client, method)(url, data)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert mock_fetch_imei_data.call_count == 0

    @pytest.mark.parametrize(
        'method, url, data, expected_status',
        [
            ('get', reverse('telegram-users:telegram-user-list'), None, status.HTTP_200_OK),
            (
                'post',
                reverse('telegram-users:telegram-user-list'),
                {'telegram_id': 123456789, 'username': 'test_user', 'name': 'Test', 'surname': 'User'},
                status.HTTP_201_CREATED,
            ),
            (
                'get',
                reverse('telegram-users:telegram-user-detail', kwargs={'telegram_id': 202022}),
                None,
                status.HTTP_404_NOT_FOUND,
            ),
            (
                'post',
                reverse('imei:check-imei'),
                {'device_id': 123456789123456},
                status.HTTP_200_OK,
            ),
        ],
    )
    @pytest.mark.usefixtures('mock_fetch_imei_data')
    def test_availability_viewset(
        self, api_client: APIClient, method: str, url: str, data: dict | None, expected_status: int, auth_param: dict
    ):
        response = getattr(api_client, method)(url, data, headers=auth_param)
        assert response.status_code == expected_status
