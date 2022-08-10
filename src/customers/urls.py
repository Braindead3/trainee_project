from django.urls import path
from rest_framework import routers
from .views import OfferViewSet, CustomerViewSet, CustomerShowroomPurchaseViewSet, UserViewSet

router = routers.SimpleRouter()

router.register(r'offer', OfferViewSet, basename='offer')
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'customer-purchase', CustomerShowroomPurchaseViewSet, basename='customer-purchase')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = router.urls

urlpatterns += [
    path('email-verify/', UserViewSet.as_view({"get": "verify_account"}), name='email_verification'),
    path('password-reset/', UserViewSet.as_view({"post": "change_password"}), name='password_reset'),
]
