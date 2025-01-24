from django.contrib import admin
from django.urls import include, path
from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='IMEI Checker',
        default_version='v1',
        description='',
    ),
    permission_classes=(AllowAny,),
    public=True,
)

api_v1 = [
    path('', include('apps.telegram.urls', namespace='telegram-users')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1)),
]
