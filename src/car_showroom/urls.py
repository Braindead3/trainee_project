from rest_framework import routers

from .views import CarShowroomViewSet, UniqueCustomerViewSet,ShowroomCustomerSaleViewSet

router = routers.SimpleRouter()
router.register(r'car-showrooms', CarShowroomViewSet, basename='car_showroom')
router.register(r'unique-customers', UniqueCustomerViewSet, basename='unique_customer')
router.register(r'showrooms-sales', ShowroomCustomerSaleViewSet, basename='showroom-customer-sale')

urlpatterns = router.urls
