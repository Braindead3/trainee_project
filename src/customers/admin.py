from django.contrib import admin
from django.db.models import Sum

from .models import Customer, CustomerShowroomPurchase, Offer
from src.car_showroom.models import ShowroomCustomerSale


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'balance', 'money_spent', 'amount_of_purchase_cars')

    def money_spent(self, obj):
        money_spent = ShowroomCustomerSale.objects.filter(customer=obj).aggregate(Sum('price'))
        return money_spent['price__sum']

    def amount_of_purchase_cars(self, obj):
        amount = ShowroomCustomerSale.objects.filter(customer=obj).count()
        return amount


admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerShowroomPurchase)
admin.site.register(Offer)
