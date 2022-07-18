from dealer.models import Car
from customers.models import Customer
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()

    class Meta:
        abstract = True


class ShowroomCars(BaseModel):
    car = models.ForeignKey(Car)
    price = models.FloatField()

    def __str__(self):
        return self.name


class SaleHistory(BaseModel):
    car = models.ForeignKey()
    customer = models.ForeignKey(Customer)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car


class UniqueCustomer(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchase_amount = models.IntegerField()

    def __str__(self):
        return self.customer


class CarShowroom(BaseModel):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    preferred_characteristics = models.JSONField()
    selected_cars = models.ForeignKey(ShowroomCars, on_delete=models.CASCADE)
    unique_customers = models.ForeignKey(UniqueCustomer, on_delete=models.CASCADE)
    balance = models.FloatField()

    def __str__(self):
        return self.name


class Discount(BaseModel):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    discount = models.IntegerField()
    car = models.ForeignKey(ShowroomCars, on_delete=models.CASCADE)
    showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.start_date
