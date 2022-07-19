from django.db import models
from djmoney.forms import MoneyField
from core.enums import Gearbox
from core.common_models import BaseModel


class Car(BaseModel):
    car_name = models.CharField(max_length=200)
    year = models.DateField()
    gearbox = models.CharField(max_length=200, choices=Gearbox)
    engine_volume = models.FloatField()
    mileage = models.PositiveIntegerField()
    color = models.CharField(max_length=200)

    def __str__(self):
        return self.car_name


class Dealer(BaseModel):
    name = models.CharField(max_length=200)
    year = models.DateField()
    customers_amount = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class CarForSale(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL)
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.car


class Discount(BaseModel):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    discount = models.IntegerField()
    car = models.ForeignKey(CarForSale, on_delete=models.SET_NULL)
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL)

    def __str__(self):
        return self.discount
