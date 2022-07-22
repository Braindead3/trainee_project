from django.contrib import admin
from .models import Car, CarForSale, Dealer, Discount, DealerShowroomSale

admin.site.register(Car)
admin.site.register(CarForSale)
admin.site.register(Dealer)
admin.site.register(Discount)
admin.site.register(DealerShowroomSale)
