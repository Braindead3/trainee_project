from django_filters import rest_framework as filters
from .models import Customer, Offer, CustomerShowroomPurchase


class CustomerViewSetFilter(filters.FilterSet):
    class Meta:
        model = Customer
        fields = {
            'name': ['icontains'],
            'address': ['icontains'],
            'balance': ['lte', 'gte'],
        }


class OfferViewSetFilter(filters.FilterSet):
    class Meta:
        model = Offer
        fields = {
            'max_price': ['lte', 'gte'],
        }


class CustomerShowroomPurchaseViewSetFilter(filters.FilterSet):
    class Meta:
        model = Offer
        fields = {
            'is_sale': ['isnull'],
            'sale_date': ['lte', 'gte'],
            'purchase_date': ['lte', 'gte'],
            'price': ['lte', 'gte'],
        }
