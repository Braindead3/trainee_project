from rest_framework import serializers
from .models import Car, Dealer, CarForSale, Discount, DealerShowroomSale


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['pk', 'name', 'year', 'gearbox', 'engine_volume', 'mileage', 'color']


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ['name', 'year', 'customers_amount', 'description', 'country', 'sales']


class CarForSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarForSale
        fields = ['car', 'dealer', 'price']


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['start_date', 'end_date', 'discount', 'dealer']


class DealerShowroomSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerShowroomSale
        fields = ['dealer', 'car_showroom', 'car', 'sale_date', 'discount']
