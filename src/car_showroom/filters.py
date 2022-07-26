from django_filters import rest_framework as filters
from .models import CarShowroom, UniqueCustomer, ShowroomCustomerSale


class CarShowroomViewSetFilter(filters.FilterSet):
    class Meta:
        model = CarShowroom
        fields = {
            'name': ['icontains'],
            'country': ['icontains'],
            'balance': ['lte', 'gte'],
        }


class UniqueCustomerViewSetFilter(filters.FilterSet):
    class Meta:
        model = UniqueCustomer
        fields = {
            'purchase_amount': ['lte', 'gte'],
        }


class ShowroomCustomerSaleViewSetFilter(filters.FilterSet):
    class Meta:
        model = UniqueCustomer
        fields = {
            'sale_date': ['lte', 'gte'],
            'price': ['lte', 'gte'],
        }
