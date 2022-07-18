from django.db import models


class Car(models.Model):
    car_name = models.CharField(max_length=200)
    year = models.DateField()
    gearbox = models.CharField(max_length=200)
    engine_volume = models.FloatField()
    mileage = models.IntegerField()


class Dealer(models.Model):
    name = models.CharField(max_length=200)
    year = models.DateField()
    customers_amount = models.IntegerField()


class CarForSale(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    price = models.FloatField()


class Discount(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    discount = models.IntegerField()
    car = models.ForeignKey(CarForSale, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)