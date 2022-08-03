from abc import ABC

from rest_framework import serializers
from .models import Customer, CustomerShowroomPurchase, Offer
from django.contrib.auth.models import User


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


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password1 = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password1 != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password1)
        user.save()
        return user


class UserUsernameSerializer(serializers.Serializer):
    username = serializers.CharField()

    class Meta:
        fields = ('username',)


class UserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ('email',)


class UserResetPasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def save(self, **kwargs):
        password1 = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password1 != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

    class Meta:
        fields = ['password1', 'password2']
