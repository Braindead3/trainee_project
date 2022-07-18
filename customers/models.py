from django.db import models
from dealer.models import CarForSale


class PurchaseHistory(models.Model):
    car = models.ForeignKey(CarForSale, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    balance = models.FloatField()
    purchase = models.ForeignKey(PurchaseHistory, on_delete=models.CASCADE)



class Offer(models.Model):
    pass