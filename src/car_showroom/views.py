from .models import CarShowroom, UniqueCustomer, ShowroomCustomerSale
from core.base_view_sets import BaseViewSet
from .serializers import CarShowroomSerializer, UniqueCustomerSerializer, ShowroomCustomerSaleSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CarShowroomViewSet(BaseViewSet):
    serializer_class = CarShowroomSerializer
    queryset = CarShowroom.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )

    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [AllowAny]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [IsLoggedInUserOrAdmin]
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]


class UniqueCustomerViewSet(BaseViewSet):
    serializer_class = UniqueCustomerSerializer
    queryset = UniqueCustomer.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ShowroomCustomerSaleViewSet(BaseViewSet):
    serializer_class = ShowroomCustomerSaleSerializer
    queryset = ShowroomCustomerSale.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
