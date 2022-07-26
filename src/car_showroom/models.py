from django.db import models
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField

from core.common_models import BaseModel


class UniqueCustomer(BaseModel):
    customer = models.ForeignKey('customers.Customer', on_delete=models.SET_NULL, null=True)
    purchase_amount = models.PositiveIntegerField()

    def __str__(self):
        return self.customer.name


class CarShowroom(BaseModel):
    name = models.CharField(max_length=200)
    country = CountryField(blank_label='(select country)')
    preferred_characteristics = models.JSONField()
    unique_customers = models.ForeignKey(UniqueCustomer, on_delete=models.SET_NULL, null=True, blank=True)
    sales = models.ManyToManyField('customers.Customer', through='ShowroomCustomerSale')
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.name


class ShowroomCustomerSale(BaseModel):
    car_showroom = models.ForeignKey(CarShowroom, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey('customers.Customer', on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey('dealer.Car', on_delete=models.SET_NULL, null=True)
    sale_date = models.DateTimeField(auto_now_add=True)
    discount = models.ForeignKey('dealer.Discount', on_delete=models.SET_NULL, null=True)
    price = MoneyField(max_digits=14, decimal_places=2, default=0, default_currency='USD')
