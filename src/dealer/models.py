from django.db import models
from djmoney.forms import MoneyField
from core.enums import Gearbox,Colors
from core.common_models import BaseModel
from django_countries.fields import CountryField
from django.db.models import CheckConstraint, Q
from src.car_showroom.models import CarShowroom


class Car(BaseModel):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    gearbox = models.CharField(max_length=200, choices=Gearbox)
    engine_volume = models.FloatField()
    mileage = models.PositiveIntegerField()
    color = models.CharField(max_length=200,choices=Colors)

    class Meta:
        constraints = (
            CheckConstraint(
                check=Q(engine_volume__gte=0.0),
                name='car_engine_volume_gte_0'),
            CheckConstraint(
                check=Q(engine_year__gte=1900),
                name='car_engine_gte_then_1900'),
        )

    def __str__(self):
        return self.name


class DealerShowroomSale(models.Model):
    car = models.ForeignKey('CarForSale', on_delete=models.SET_NULL)
    sale_date = models.DateTimeField(auto_now_add=True)
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL)


class Dealer(BaseModel):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    customers_amount = models.PositiveIntegerField()
    description = models.TextField()
    country = CountryField()
    sales = models.ManyToManyField(CarShowroom, through=DealerShowroomSale)

    def __str__(self):
        return self.name


class CarForSale(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL)
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.car
