from .models import Customer, Offer, CustomerShowroomPurchase
from core.base_view_sets import BaseViewSet
from .serializers import CustomerSerializer, OfferSerializer, CustomerShowroomPurchaseSerializer


class CustomerViewSet(BaseViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class OfferViewSet(BaseViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class CustomerShowroomPurchaseViewSet(BaseViewSet):
    serializer_class = CustomerShowroomPurchaseSerializer
    queryset = CustomerShowroomPurchase.objects.all()
