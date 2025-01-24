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
            'created',
            'updated',
        ]
        read_only_fields = [
            'created',
            'updated',
        ]
