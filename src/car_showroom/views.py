from .models import CarShowroom, UniqueCustomer, ShowroomCustomerSale
from core.base_view_sets import BaseViewSet
from .serializers import CarShowroomSerializer, UniqueCustomerSerializer, ShowroomCustomerSaleSerializer


class CarShowroomViewSet(BaseViewSet):
    serializer_class = CarShowroomSerializer
    queryset = CarShowroom.objects.all()


class UniqueCustomerViewSet(BaseViewSet):
    serializer_class = UniqueCustomerSerializer
    queryset = UniqueCustomer.objects.all()


class ShowroomCustomerSaleViewSet(BaseViewSet):
    serializer_class = ShowroomCustomerSaleSerializer
    queryset = ShowroomCustomerSale.objects.all()
