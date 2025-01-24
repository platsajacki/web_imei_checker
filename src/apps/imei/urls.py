from django.urls import path

from apps.imei.api.viewsets import IMEIView

app_name = 'imei'

urlpatterns = [
    path('check-imei/', IMEIView.as_view(), name='check-imei'),
]
