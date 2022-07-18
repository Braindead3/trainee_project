from django.db import models
from car_showroom.models import ShowroomCars, BaseModel
from dealer.models import Car


class PurchaseHistory(BaseModel):
    car = models.ForeignKey(ShowroomCars, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car


class Customer(BaseModel):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    balance = models.FloatField()
    purchase = models.ForeignKey(PurchaseHistory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Offer(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    max_price = models.FloatField()

    def __str__(self):
        return self.car
