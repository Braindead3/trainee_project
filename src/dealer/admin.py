from django.contrib import admin
from django.db.models import Sum

from .models import Car, CarForSale, Dealer, Discount, DealerShowroomSale


class DealerAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "description", "country", 'amount_of_sold_cars', 'earnings', 'unique_showrooms')

    def amount_of_sold_cars(self, obj):
        result = DealerShowroomSale.objects.filter(dealer=obj).count()
        return result

    def earnings(self, obj):
        dealer_sales = DealerShowroomSale.objects.filter(dealer=obj).aggregate(Sum('price'))
        return dealer_sales['price__sum']

    def unique_showrooms(self, obj):
        count_of_showrooms = DealerShowroomSale.objects.filter(dealer=obj).order_by('car_showroom').distinct(
            'car_showroom').count()
        return count_of_showrooms


admin.site.register(Car)
admin.site.register(CarForSale)
admin.site.register(Dealer, DealerAdmin)
admin.site.register(Discount)
admin.site.register(DealerShowroomSale)
