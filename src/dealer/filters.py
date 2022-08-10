from django_filters import rest_framework as filters
from .models import Car, Dealer, CarForSale, Discount, DealerShowroomSale


class CarViewSetFilter(filters.FilterSet):
    class Meta:
        model = Car
        fields = {
            'name': ['icontains'],
            'year': ['lte', 'gte'],
            'color': ['iexact'],
            'mileage': ['lte', 'gte']
        }


class DiscountViewSetFilter(filters.FilterSet):
    class Meta:
        model = Discount
        fields = {
            'start_date': ['lte', 'gte'],
            'end_date': ['lte', 'gte'],
            'discount': ['lte', 'gte'],
        }


class DealerViewSetFilter(filters.FilterSet):
    class Meta:
        model = Dealer
        fields = {
            'name': ['icontains'],
            'year': ['lte', 'gte'],
            'customers_amount': ['lte', 'gte'],
            'country': ['icontains'],
        }


class CarForSaleViewSetFilter(filters.FilterSet):
    class Meta:
        model = CarForSale
        fields = {
            'price': ['lte', 'gte'],
        }


class DealerShowroomSaleViewSetFilter(filters.FilterSet):
    class Meta:
        model = DealerShowroomSale
        fields = {
            'sale_date': ['lte', 'gte'],
            'discount': ['lte', 'gte'],
            'price': ['lte', 'gte'],
        }
