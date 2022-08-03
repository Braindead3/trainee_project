from django.db.models import Sum

from .models import DealerShowroomSale


def get_amount_of_sold_cars(dealer_id):
    dealer_sales = DealerShowroomSale.objects.filter(dealer=dealer_id)
    if dealer_sales:
        return dealer_sales.count()
    return 'Dealer does not exists'


def get_earnings(dealer_id):
    dealer_sales = DealerShowroomSale.objects.filter(dealer=dealer_id)
    if dealer_sales:
        earnings = dealer_sales.aggregate(Sum('price'))
        return earnings
    return 'Dealer does not exists'


def get_amount_of_showrooms(dealer_id):
    dealer_sales = DealerShowroomSale.objects.filter(dealer=dealer_id)
    if dealer_sales:
        return dealer_sales.order_by('car_showroom').distinct('car_showroom').count()
    return 'Dealer do not have unique showrooms'
