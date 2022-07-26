from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .filters import CarShowroomViewSetFilter, UniqueCustomerViewSetFilter, ShowroomCustomerSaleViewSetFilter
from .models import CarShowroom, UniqueCustomer, ShowroomCustomerSale
from .serializers import CarShowroomSerializer, UniqueCustomerSerializer, ShowroomCustomerSaleSerializer


class CarShowroomViewSet(viewsets.ModelViewSet):
    serializer_class = CarShowroomSerializer
    queryset = CarShowroom.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_class = CarShowroomViewSetFilter
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['balance', 'country', 'name']

    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [AllowAny]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [IsLoggedInUserOrAdmin]
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]


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
