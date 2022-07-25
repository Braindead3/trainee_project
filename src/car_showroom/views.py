from .models import CarShowroom, UniqueCustomer, ShowroomCustomerSale
from core.base_view_sets import BaseViewSet
from .serializers import CarShowroomSerializer, UniqueCustomerSerializer, ShowroomCustomerSaleSerializer
from rest_framework.permissions import IsAuthenticated


class CarShowroomViewSet(BaseViewSet):
    serializer_class = CarShowroomSerializer
    queryset = CarShowroom.objects.all()
    permission_classes = [IsAuthenticated, ]


class UniqueCustomerViewSet(BaseViewSet):
    serializer_class = UniqueCustomerSerializer
    queryset = UniqueCustomer.objects.all()
    permission_classes = [IsAuthenticated, ]


class ShowroomCustomerSaleViewSet(BaseViewSet):
    serializer_class = ShowroomCustomerSaleSerializer
    queryset = ShowroomCustomerSale.objects.all()
    permission_classes = [IsAuthenticated, ]
