import re

from rest_framework import serializers


class DeviceSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)

    def validate_device_id(self, value: str) -> str:
        """Проверка на соответствие формату IMEI (15 цифр) или серийного номера (8-14 любых символов)"""
        imei_pattern = re.compile(r'^\d{15}$')
        serial_number_pattern = re.compile(r'^[a-zA-Z0-9]{8,14}$')
        if not (imei_pattern.fullmatch(value) or serial_number_pattern.fullmatch(value)):
            raise serializers.ValidationError(
                'Идентификатор должен быть IMEI (15 цифр) или серийным номером (8-14 символов: буквы и цифры).'
            )
        return value
