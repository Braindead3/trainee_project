from rest_framework import routers
from .views import (OfferViewSet, DealerViewSet, CarForSaleViewSet, DealerShowroomSaleViewSet,
                    CarViewSet)

router = routers.SimpleRouter()

router.register(r'cars', CarViewSet, basename='car')
router.register(r'offers', OfferViewSet, basename='offer')
router.register(r'dealers', DealerViewSet, basename='dealer')
router.register(r'cars-for-sale', CarForSaleViewSet, basename='car')
router.register(r'dealer-sales', DealerShowroomSaleViewSet, basename='dealer-sales')

urlpatterns = router.urls
