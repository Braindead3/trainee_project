from django.db import models
from djmoney.forms import MoneyField

from src.car_showroom.models import Discount, CarShowroom
from core.common_models import BaseModel
from src.dealer.models import Car


class CustomerShowroomPurchase(BaseModel):
    purchase_date = models.DateTimeField(auto_now_add=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL)
    is_sale = models.BooleanField(blank=True)
    sale_date = models.DateField(blank=True)


class Customer(BaseModel):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    purchase = models.ManyToManyField(CarShowroom, on_delete=models.SET_NULL, through='ShowroomCustomerPurchase')

    def __str__(self):
        return self.name


class Offer(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL)
    max_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.car
