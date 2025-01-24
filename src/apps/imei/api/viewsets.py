from typing import Any

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.imei.api.serializers import DeviceSerializer
from apps.imei.schemas import IMEIViewSwagger
from apps.imei.services.imei_checker import IMEIChecker


class IMEIView(APIView):
    """Обработчик запросов для проверки IMEI или серийного номера устройства."""

    @IMEIViewSwagger.post()
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Обрабатывает POST-запрос для проверки IMEI."""
        return IMEIChecker(DeviceSerializer(data=request.data))()
