from rest_framework import viewsets

from .filters import CarViewSetFilter, DiscountViewSetFilter, DealerViewSetFilter, CarForSaleViewSetFilter, \
    DealerShowroomSaleViewSetFilter
from .models import Car, Dealer, CarForSale, Discount, DealerShowroomSale
from .serializers import (CarSerializer, DiscountSerializer, DealerSerializer,
                          DealerShowroomSaleSerializer, CarForSaleSerializer)


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    filterset_class = CarViewSetFilter

    def get_queryset(self):
        sorting_field = self.request.GET.get('sort_field')
        if sorting_field is not None:
            return Car.objects.order_by(sorting_field)
        return Car.objects.all()


class DiscountViewSet(viewsets.ModelViewSet):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
    filterset_class = DiscountViewSetFilter

    def get_queryset(self):
        sorting_field = self.request.GET.get('sort_field')
        if sorting_field is not None:
            return Discount.objects.order_by(sorting_field)
        return Discount.objects.all()


class DealerViewSet(viewsets.ModelViewSet):
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()
    filterset_class = DealerViewSetFilter

    def get_queryset(self):
        sorting_field = self.request.GET.get('sort_field')
        if sorting_field is not None:
            return Dealer.objects.order_by(sorting_field)
        return Dealer.objects.all()


class CarForSaleViewSet(viewsets.ModelViewSet):
    serializer_class = CarForSaleSerializer
    queryset = CarForSale.objects.all()
    filterset_class = CarForSaleViewSetFilter

    def get_queryset(self):
        sorting_field = self.request.GET.get('sort_field')
        if sorting_field is not None:
            return CarForSale.objects.order_by(sorting_field)
        return CarForSale.objects.all()


class DealerShowroomSaleViewSet(viewsets.ModelViewSet):
    serializer_class = DealerShowroomSaleSerializer
    queryset = DealerShowroomSale.objects.all()
    filterset_class = DealerShowroomSaleViewSetFilter

    def get_queryset(self):
        sorting_field = self.request.GET.get('sort_field')
        if sorting_field is not None:
            return sorting_field.objects.order_by(sorting_field)
        return sorting_field.objects.all()
