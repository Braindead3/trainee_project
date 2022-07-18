from dealer.models import Car
from customers.models import Customer
from django.db import models


class ShowroomCars(models.Model):
    car = models.ForeignKey(Car)
    price = models.FloatField()

    def __str__(self):
        return self.name


class SaleHistory(models.Model):
    car = models.ForeignKey()
    customer = models.ForeignKey(Customer)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car


class UniqueCustomer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchase_amount = models.IntegerField()

    def __str__(self):
        return self.customer


class CarShowroom(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    preferred_characteristics = models.JSONField()
    selected_cars = models.ForeignKey(ShowroomCars, on_delete=models.CASCADE)
    unique_customers = models.ForeignKey(UniqueCustomer, on_delete=models.CASCADE)
    balance = models.FloatField()

    def __str__(self):
        return self.name


class Discount(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    discount = models.IntegerField()
    car = models.ForeignKey(ShowroomCars, on_delete=models.CASCADE)
    showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.start_date
