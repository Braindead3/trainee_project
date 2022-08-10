from django.contrib import admin
from django.db.models import Sum

from .models import UniqueCustomer, CarShowroom, ShowroomCustomerSale, ShowroomCarsForSale


class CarShowroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'balance', 'amount_of_sold_cars', 'earnings', 'amount_of_unique_customers')

    def amount_of_sold_cars(self, obj):
        amount = ShowroomCustomerSale.objects.filter(car_showroom=obj).count()
        return amount

    def earnings(self, obj):
        earnings = ShowroomCustomerSale.objects.filter(car_showroom=obj).aggregate(Sum('price'))
        return earnings['price__sum']

    def amount_of_unique_customers(self, obj):
        unique_customers = UniqueCustomer.objects.filter(customer_showroom=obj).count()
        return unique_customers


admin.site.register(UniqueCustomer)
admin.site.register(CarShowroom, CarShowroomAdmin)
admin.site.register(ShowroomCustomerSale)
admin.site.register(ShowroomCarsForSale)
