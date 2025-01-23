from django.contrib import admin
from django.forms import Form
from django.http import HttpRequest

from apps.api_keys.models import APIKey


@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
        'updated',
    )
    fields = (
        'name',
        'key',
    )

    def save_model(self, request: HttpRequest, obj: APIKey, form: Form, change: bool) -> None:
        if not obj.key:
            obj.key = obj.generate_key()
        super().save_model(request, obj, form, change)
