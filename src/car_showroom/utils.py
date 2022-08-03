from django.shortcuts import get_object_or_404

from .models import CarShowroom, ShowroomCustomerSale, UniqueCustomer
from django.db.models import Sum


def get_amount_of_sold_cars(showroom_id):
    showroom = CarShowroom.objects.filter(pk=showroom_id).first()
    if showroom:
        return showroom.sales.count()
    return 'Showroom does not exists'


def get_amount_of_earnings(showroom_id):
    showroom = CarShowroom.objects.filter(pk=showroom_id).first()
    if showroom:
        earnings = ShowroomCustomerSale.objects.filter(car_showroom=showroom).aggregate(Sum('price'))
        return earnings
    return 'Showroom does not exists'


def get_amount_of_unique_customer(showroom_id):
    unique_customers = UniqueCustomer.objects.filter(customer_showroom=showroom_id)
    if unique_customers:
        return unique_customers.count()
    return 'Showroom do not have unique customers'
