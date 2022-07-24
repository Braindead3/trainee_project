from rest_framework import routers
from .views import OfferViewSet, CustomerViewSet, CustomerShowroomPurchaseViewSet

router = routers.SimpleRouter()

router.register(r'offer', OfferViewSet, basename='offer')
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'customer-purchase', CustomerShowroomPurchaseViewSet, basename='customer-purchase')

urlpatterns = router.urls
