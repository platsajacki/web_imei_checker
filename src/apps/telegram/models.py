from django.db import models

from core.models import TimestampedModel


class TelegramUser(TimestampedModel):
    """Пользователи, которые могут использовать телеграм бота."""

    name = models.CharField(
        verbose_name='Name',
        max_length=255,
    )
    surname = models.CharField(
        verbose_name='Surname',
        max_length=255,
    )
    telegram_id = models.BigIntegerField(
        verbose_name='Telegram ID',
        unique=True,
    )
    is_allowed = models.BooleanField(
        verbose_name='Access allowed',
        default=True,
    )

    class Meta:
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram Users'
        ordering = ['-created']

    def __str__(self) -> str:
        return f'{self.name} {self.surname}. ID: {self.telegram_id}'
