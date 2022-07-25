from rest_framework import serializers
from .models import Customer, CustomerShowroomPurchase, Offer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['pk', 'name', 'address', 'balance', 'purchase']


class CustomerShowroomPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerShowroomPurchase
        fields = ['customer', 'car_showroom', 'discount', 'car', 'is_sale', 'sale_date']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['car', 'customer', 'max_price']
