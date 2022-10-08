from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from firmware.api.views import GetErrorLogs


class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/logs/", GetErrorLogs.as_view(), name="error-logs"),
    path("api/login", TokenObtainPairView.as_view(), name="login"),
    path("api/token-refresh", TokenRefreshView.as_view(), name="refresh-token"),
    path("api/users/", include("users.urls", namespace="users"), name="users"),
    path(
        "api/firmware/", include("firmware.urls", namespace="firmware"), name="firmware"
    ),
    path(
        "api/emulator/", include("emulator.urls", namespace="emulator"), name="emulator"
    ),
]

if settings.API_ENABLED:

    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view

    schema_view = get_schema_view(
        openapi.Info(
            title="FirmwareSecurity API",
            default_version="v1",
            description="API DOCS",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        authentication_classes=(JWTAuthentication,),
    )

    urlpatterns += [
        re_path(
            r"^api/swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"^api/swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        re_path(
            r"^api/redoc/$",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
