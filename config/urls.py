
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('src.car_showroom.urls'), name='car_showroom-viewset'),
    # path('api/', include('src.customers.urls'), name='customer-viewset'),
    # path('api/', include('src.dealer.urls'), name='dealer-viewset'),
]