from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from .filters import CarViewSetFilter, DiscountViewSetFilter, DealerViewSetFilter, CarForSaleViewSetFilter, \
    DealerShowroomSaleViewSetFilter
from .models import Car, Dealer, CarForSale, Discount, DealerShowroomSale
from .serializers import (CarSerializer, DiscountSerializer, DealerSerializer,
                          DealerShowroomSaleSerializer, CarForSaleSerializer)
from src.dealer.utils import get_amount_of_sold_cars, get_earnings, get_amount_of_showrooms


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    filterset_class = CarViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ('name',)
    ordering_fields = ('name', 'year', 'engine_volume', 'mileage')


class DiscountViewSet(viewsets.ModelViewSet):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
    filterset_class = DiscountViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ('dealer__name',)
    ordering_fields = ('start_date', 'end_date', 'discount')


class DealerViewSet(viewsets.ModelViewSet):
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()
    filterset_class = DealerViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ('dealer__name', 'car_showroom__name', 'car__name')
    ordering_fields = ('start_date', 'end_date', 'discount', 'price')

    @action(methods=('get',), detail=True)
    def amount_of_sold_cars(self, request, pk):
        if pk:
            amount_of_cars = get_amount_of_sold_cars(pk)
            return Response({'amount of sold cars': amount_of_cars})
        return Response('pk not provided or dealer does not exist')

    @action(methods=('get',), detail=True)
    def amount_of_earnings(self, request, pk):
        if pk:
            earnings = get_earnings(pk)
            return Response({'amount of sold cars': earnings})
        return Response('pk not provided or dealer does not exist')

    @action(methods=('get',), detail=True)
    def amount_of_showrooms(self, request, pk):
        if pk:
            amount_of_showrooms = get_amount_of_showrooms(pk)
            return Response({'amount of showrooms': amount_of_showrooms})
        return Response('pk not provided or dealer does not exist')


class CarForSaleViewSet(viewsets.ModelViewSet):
    serializer_class = CarForSaleSerializer
    queryset = CarForSale.objects.all()
    filterset_class = CarForSaleViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ('car__name', 'dealer__name')
    ordering_fields = ('price',)


class DealerShowroomSaleViewSet(viewsets.ModelViewSet):
    serializer_class = DealerShowroomSaleSerializer
    queryset = DealerShowroomSale.objects.all().select_related('car_showroom')
    filterset_class = DealerShowroomSaleViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ('car_showroom__name', 'dealer__name', 'car__name')
    ordering_fields = ('sale_date', 'discount', 'price')
