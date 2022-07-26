from rest_framework import viewsets

from .filters import CarShowroomViewSetFilter, UniqueCustomerViewSetFilter, ShowroomCustomerSaleViewSetFilter
from .models import CarShowroom, UniqueCustomer, ShowroomCustomerSale
from .serializers import CarShowroomSerializer, UniqueCustomerSerializer, ShowroomCustomerSaleSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CarShowroomViewSet(viewsets.ModelViewSet):
    serializer_class = CarShowroomSerializer
    queryset = CarShowroom.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filterset_class = CarShowroomViewSetFilter

    def get_queryset(self):
        sorting_field = self.request.GET.get('sort_field')
        if sorting_field is not None:
            return CarShowroom.objects.order_by(sorting_field)
        return CarShowroom.objects.all()

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
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filterset_class = UniqueCustomerViewSetFilter

    def get_queryset(self):
        sorting_field = self.request.GET.get('sort_field')
        if sorting_field is not None:
            return UniqueCustomer.objects.order_by(sorting_field)
        return UniqueCustomer.objects.all()


class ShowroomCustomerSaleViewSet(viewsets.ModelViewSet):
    serializer_class = ShowroomCustomerSaleSerializer
    queryset = ShowroomCustomerSale.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filterset_class = ShowroomCustomerSaleViewSetFilter

    def get_queryset(self):
        sorting_field = self.request.GET.get('sort_field')
        if sorting_field is not None:
            return ShowroomCustomerSale.objects.order_by(sorting_field)
        return ShowroomCustomerSale.objects.all()
