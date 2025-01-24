from django.db import models


class TimestampedModel(models.Model):
    """Абстарктная модель с полями 'created' и 'updated'."""

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at',
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Udated at',
    )

    class Meta:
        abstract = True
