from rest_framework import serializers

from apps.telegram.models import TelegramUser


class TelegramUserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели TelegramUser."""

    class Meta:
        model = TelegramUser
        fields = [
            'name',
            'surname',
            'telegram_id',
            'is_allowed',
            'created',
            'updated',
        ]
        read_only_fields = [
            'is_allowed',
            'created',
            'updated',
        ]
