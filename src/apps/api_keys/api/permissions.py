from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request
from rest_framework.views import View

from apps.api_keys.models import APIKey


class TokenPermission(permissions.BasePermission):
    """Пермишн для проверки API Key."""

    def has_permission(self, request: Request, view: View) -> bool:
        token = request.data.get('token')
        if not token:
            raise AuthenticationFailed('Token not found.')
        try:
            APIKey.objects.get(key=token)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed()
        return True
