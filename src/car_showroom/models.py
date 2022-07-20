from django.db.models import CheckConstraint, Q
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
from core.common_models import BaseModel
from src.dealer.models import Car, Dealer
from src.customers.models import Customer
from django.db import models


class ShowroomCars(BaseModel):
    car = models.ForeignKey(Car)
    price = MoneyField(max_digits=14, decimal_places=2, default=0, default_currency='USD')

    def __str__(self):
        return self.name


class ShowroomCustomerSale(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL)
    sale_date = models.DateTimeField(auto_now_add=True)
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL)


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
    sales = models.ManyToManyField(Customer, through=ShowroomCustomerSale)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.name


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
        return self.start_date
