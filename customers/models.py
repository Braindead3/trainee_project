from django.db import models
from car_showroom.models import ShowroomCars
from dealer.models import Car


class PurchaseHistory(models.Model):
    car = models.ForeignKey(ShowroomCars, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car


class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    balance = models.FloatField()
    purchase = models.ForeignKey(PurchaseHistory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Offer(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    max_price = models.FloatField()

    def __str__(self):
        return self.car
