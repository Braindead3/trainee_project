from django.contrib import admin
from .models import UniqueCustomer, CarShowroom, ShowroomCustomerSale

admin.site.register(UniqueCustomer)
admin.site.register(CarShowroom)
admin.site.register(ShowroomCustomerSale)
