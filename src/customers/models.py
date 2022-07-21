from django.db import models
from djmoney.forms import MoneyField
from core.common_models import BaseModel


class Customer(BaseModel):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    purchase = models.ManyToManyField('car_showroom.CarShowroom', through='CustomerShowroomPurchase')

    def __str__(self):
        return self.name


class CustomerShowroomPurchase(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    car_showroom = models.ForeignKey('car_showroom.CarShowroom', on_delete=models.SET_NULL, null=True)
    discount = models.ForeignKey('dealer.Discount', on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey('dealer.Car', on_delete=models.SET_NULL, null=True)
    is_sale = models.BooleanField(blank=True)
    sale_date = models.DateField(blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)


class Offer(BaseModel):
    car = models.ForeignKey('dealer.Car', on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    max_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.car
