from django.core.validators import MinValueValidator
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
from core.common_models import BaseModel
from src.dealer.models import Car
from src.customers.models import Customer
from django.db import models


class ShowroomCars(BaseModel):
    car = models.ForeignKey(Car)
    price = MoneyField(max_digits=14, decimal_places=2, default=0, default_currency='USD')

    def __str__(self):
        return self.name


class History(BaseModel):
    sale_date = models.DateTimeField(auto_now_add=True)
    discount = models.ForeignKey('Discount')


class Sale(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL)

    def __str__(self):
        return self.car


class UniqueCustomer(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL)
    purchase_amount = models.PositiveIntegerField()

    def __str__(self):
        return self.customer


class CarShowroom(BaseModel):
    name = models.CharField(max_length=200)
    country = CountryField(blank_label='(select country)')
    preferred_characteristics = models.JSONField()
    selected_cars = models.ForeignKey(ShowroomCars, on_delete=models.SET_NULL)
    unique_customers = models.ForeignKey(UniqueCustomer, on_delete=models.SET_NULL)
    sales = models.ManyToManyField(Sale, on_delete=models.SET_NULL, through=History)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.name


class Discount(BaseModel):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    discount = models.IntegerField()

    def __str__(self):
        return self.start_date
