from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from .filters import CustomerViewSetFilter, OfferViewSetFilter, CustomerShowroomPurchaseViewSetFilter
from .models import Customer, Offer, CustomerShowroomPurchase
from .serializers import CustomerSerializer, OfferSerializer, CustomerShowroomPurchaseSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filterset_class = CustomerViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['name', 'address']
    ordering_fields = ['balance', 'name']


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    filterset_class = OfferViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['car__name', 'customer__name']
    ordering_fields = ['max_price']


class CustomerShowroomPurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerShowroomPurchaseSerializer
    queryset = CustomerShowroomPurchase.objects.all()
    filterset_class = CustomerShowroomPurchaseViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['customer__name']
    ordering_fields = ['is_sale', 'sale_date', 'purchase_date', 'price']
