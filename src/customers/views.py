from rest_framework import viewsets

from .filters import CustomerViewSetFilter, OfferViewSetFilter, CustomerShowroomPurchaseViewSetFilter
from .models import Customer, Offer, CustomerShowroomPurchase

from .serializers import CustomerSerializer, OfferSerializer, CustomerShowroomPurchaseSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filterset_class = CustomerViewSetFilter

    def get_queryset(self):
        sorting_field = self.request.GET.get('sort_field')
        if sorting_field is not None:
            return Customer.objects.order_by(sorting_field)
        return Customer.objects.all()


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    filterset_class = OfferViewSetFilter

    def get_queryset(self):
        sorting_field = self.request.GET.get('sort_field')
        if sorting_field is not None:
            return Offer.objects.order_by(sorting_field)
        return Offer.objects.all()


class CustomerShowroomPurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerShowroomPurchaseSerializer
    queryset = CustomerShowroomPurchase.objects.all()
    filterset_class = CustomerShowroomPurchaseViewSetFilter

    def get_queryset(self):
        sorting_field = self.request.GET.get('sort_field')
        if sorting_field is not None:
            return CustomerShowroomPurchase.objects.order_by(sorting_field)
        return CustomerShowroomPurchase.objects.all()
