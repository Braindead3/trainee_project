from rest_framework import serializers
from .models import CarShowroom, UniqueCustomer, ShowroomCustomerSale


class CarShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroom
        fields = ['pk', 'name', 'country', 'preferred_characteristics', 'balance']


class UniqueCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueCustomer
        fields = ['customer', 'purchase_amount']


class ShowroomCustomerSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomCustomerSale
        fields = ['car_showroom', 'customer', 'car', 'sale_date', 'discount', 'price']
