import pytest

from rest_framework.exceptions import ValidationError

from apps.imei.api.serializers import DeviceSerializer


@pytest.mark.parametrize(
    'device_id',
    [
        '123456789012345',
        'ABC123XYZ',
        'ABCDEFGHIJKLMN',
        '1234ABCD12',
    ],
)
def test_valid_device_ids(device_id):
    data = {'device_id': device_id}
    serializer = DeviceSerializer(data=data)
    assert serializer.is_valid()


@pytest.mark.parametrize(
    'device_id',
    [
        '12345XY',
        'ABC123XYZ!',
        '',
        '12345678901234562',
        '1234_ABCD',
    ],
)
def test_invalid_device_ids(device_id):
    data = {'device_id': device_id}
    serializer = DeviceSerializer(data=data)
    assert not serializer.is_valid()
    assert 'device_id' in serializer.errors


def test_invalid_device_id_raises_validation_error():
    serializer = DeviceSerializer(data={'device_id': 'wrong_id'})
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)
