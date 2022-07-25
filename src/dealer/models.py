from django.db import models
from django.db.models import CheckConstraint, Q
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField

from core.common_models import BaseModel


class Car(BaseModel):
    class Gearbox(models.TextChoices):
        Automatic = 'automatic', 'automatic'
        Manual = 'manual', 'manual'

    class Colors(models.TextChoices):
        Red = 'red', 'red'
        Yellow = 'yellow', 'yellow'
        Blue = 'blue', 'blue'
        Black = 'black', 'black'
        White = 'white', 'white'

    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    gearbox = models.CharField(max_length=200, choices=Gearbox.choices)
    engine_volume = models.FloatField()
    mileage = models.PositiveIntegerField()
    color = models.CharField(max_length=200, choices=Colors.choices)

    class Meta:
        constraints = (
            CheckConstraint(
                check=Q(engine_volume__gte=0.0),
                name='car_engine_volume_gte_0'),
            CheckConstraint(
                check=Q(year__gte=1900),
                name='car_year_gte_then_1900'),
        )

    def __str__(self):
        return self.name


class Dealer(BaseModel):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    customers_amount = models.PositiveIntegerField()
    description = models.TextField()
    country = CountryField()
    sales = models.ManyToManyField('car_showroom.CarShowroom', through='DealerShowroomSale')

    def __str__(self):
        return self.name


class CarForSale(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL, null=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True, null=True)

    def __str__(self):
        return self.car.name + ' ' + self.dealer.name


class Discount(BaseModel):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    discount = models.PositiveIntegerField()
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        constraints = (
            CheckConstraint(
                check=Q(discount__gte=0) & Q(discount__lte=100),
                name='discount_in_range_of_0_100'),
        )

    def __str__(self):
        return self.dealer.name


class DealerShowroomSale(BaseModel):
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL, null=True)
    car_showroom = models.ForeignKey('car_showroom.CarShowroom', on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(CarForSale, on_delete=models.SET_NULL, null=True)
    sale_date = models.DateTimeField(auto_now_add=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True)
    price = MoneyField(max_digits=14, decimal_places=2, default=0, default_currency='USD', blank=True, null=True)

    def __str__(self):
        return self.dealer.name
