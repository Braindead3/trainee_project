
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/models/', include('src.car_showroom.urls'), name='car-showroom-models'),
    path('api/models/', include('src.customers.urls'), name='customer-models'),
    path('api/models/', include('src.dealer.urls'), name='dealer-models'),
]