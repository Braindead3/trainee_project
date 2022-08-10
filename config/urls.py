from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title='My test API',
        default_version='1.0.0',
        description='API documentation of App'
    ),
    public=True,
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
    path('__debug__/', include('debug_toolbar.urls')),

    path('admin/', admin.site.urls),

    path('api/car_showroom/', include('src.car_showroom.urls'), name='car-showroom-models'),
    path('api/customers/', include('src.customers.urls'), name='customer-models'),
    path('api/dealer/', include('src.dealer.urls'), name='dealer-models'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
