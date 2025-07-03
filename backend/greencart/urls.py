from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="GreenCart API",
        default_version="v1",
        description="This is the greencart api, it populates GreenCart site",
        #terms_of_service=
        contact=openapi.Contact(email="greencart.ecotrybe@gmail.com"),
        license=openapi.License(name="BSD License"),
        public=True)
)
#openapi.Info()
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("base.urls")),
    path("api/v1/auth/", include("users.urls")),
    path("api/v1/cart/", include("cart.urls")),
    path("api/v1/greenbin/", include("greenbin.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]