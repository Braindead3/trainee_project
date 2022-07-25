from .models import Car, Dealer, CarForSale, Discount, DealerShowroomSale
from core.base_view_sets import BaseViewSet
from .serializers import (CarSerializer, DiscountSerializer, DealerSerializer,
                          DealerShowroomSaleSerializer, CarForSaleSerializer)


class CarViewSet(BaseViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class OfferViewSet(BaseViewSet):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()


class DealerViewSet(BaseViewSet):
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()


class CarForSaleViewSet(BaseViewSet):
    serializer_class = CarForSaleSerializer
    queryset = CarForSale.objects.all()


class DealerShowroomSaleViewSet(BaseViewSet):
    serializer_class = DealerShowroomSaleSerializer
    queryset = DealerShowroomSale.objects.all()
