from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .filters import CarShowroomViewSetFilter, UniqueCustomerViewSetFilter, ShowroomCustomerSaleViewSetFilter
from .models import CarShowroom, UniqueCustomer, ShowroomCustomerSale
from .serializers import CarShowroomSerializer, UniqueCustomerSerializer, ShowroomCustomerSaleSerializer
from .utils import get_amount_of_sold_cars,get_amount_of_earnings,get_amount_of_unique_customer


class CarShowroomViewSet(viewsets.ModelViewSet):
    serializer_class = CarShowroomSerializer
    queryset = CarShowroom.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_class = CarShowroomViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['balance', 'country', 'name']

    @action(methods=['get'], detail=True)
    def amount_of_sold_cars(self, request, pk):
        if pk:
            amount_of_cars = get_amount_of_sold_cars(pk)
            return Response({'amount of sold cars': amount_of_cars})
        return Response('pk not provided')

    @action(methods=['get'], detail=True)
    def amount_of_earnings(self, request, pk):
        if pk:
            amount_of_earnings = get_amount_of_earnings(pk)
            return Response({'amount of earnings': amount_of_earnings})
        return Response('pk not provided or showroom does not exist')

    @action(methods=['get'], detail=True)
    def amount_of_unique_customers(self, request, pk):
        if pk:
            amount_of_unique_customers = get_amount_of_unique_customer(pk)
            return Response({'amount of unique customers': amount_of_unique_customers})
        return Response('pk not provided or showroom does not exist')


class UniqueCustomerViewSet(viewsets.ModelViewSet):
    serializer_class = UniqueCustomerSerializer
    queryset = UniqueCustomer.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_class = UniqueCustomerViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['customer__name']
    ordering_fields = ['purchase_amount']


class ShowroomCustomerSaleViewSet(viewsets.ModelViewSet):
    serializer_class = ShowroomCustomerSaleSerializer
    queryset = ShowroomCustomerSale.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_class = ShowroomCustomerSaleViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['car_showroom__name', 'customer__name', 'car__name']
    ordering_fields = ['price', 'sale_date']
