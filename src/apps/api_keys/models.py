import secrets

from django.db import models

from core.models import TimestampedModel


class APIKey(TimestampedModel):
    """Модель для хранения API-ключей с возможностью их автоматической генерации."""

    name = models.CharField(
        max_length=255,
        verbose_name='Name',
        unique=True,
    )
    key = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='API Key',
        editable=False,
    )

    class Meta:
        verbose_name = 'API Key'
        verbose_name_plural = 'API Keys'
        ordering = ['-created']

    def __str__(self) -> str:
        return f'{self.name} API Key: {self.key[:5]}...'

    def save(self, *args, **kwargs) -> None:
        """Генерация API-ключа при создании объекта."""
        if not self.key:
            self.key = self.generate_key()
        super().save(*args, **kwargs)

    def generate_key(self) -> str:
        """Генерация нового API-ключа."""
        return secrets.token_hex(32)
