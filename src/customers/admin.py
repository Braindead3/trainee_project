from django.contrib import admin
from django.db.models import Sum, Count

from .models import Customer, CustomerShowroomPurchase, Offer
from src.car_showroom.models import ShowroomCustomerSale
from src.dealer.models import Car


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'balance', 'money_spent', 'amount_of_purchase_cars','favorite_car')

    def money_spent(self, obj):
        money_spent = ShowroomCustomerSale.objects.filter(customer=obj).aggregate(Sum('price'))
        return money_spent['price__sum']

    def amount_of_purchase_cars(self, obj):
        amount = ShowroomCustomerSale.objects.filter(customer=obj).count()
        return amount

    def favorite_car(self, obj):
        favorite_car = ShowroomCustomerSale.objects.filter(customer=obj).values('car').annotate(count_cars=Count('car')).order_by(
            '-count_cars').first()
        car = Car.objects.get(pk=favorite_car['car'])
        return car


admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerShowroomPurchase)
admin.site.register(Offer)
