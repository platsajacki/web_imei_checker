from django.contrib import admin

from .models import TelegramUser


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    """Админ-панель для управления пользователями Telegram."""

    list_display = (
        'id',
        'name',
        'surname',
        'telegram_id',
        'created',
        'updated',
    )
    search_fields = (
        'name',
        'surname',
        'telegram_id',
    )
    list_filter = (
        'created',
        'updated',
    )
    ordering = ('-created',)
    readonly_fields = (
        'created',
        'updated',
    )
