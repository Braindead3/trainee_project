
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/models/', include('src.car_showroom.urls'), name='car-showroom-models'),
    path('api/models/', include('src.customers.urls'), name='customer-models'),
    path('api/models/', include('src.dealer.urls'), name='dealer-models'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]