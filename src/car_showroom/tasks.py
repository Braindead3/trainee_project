from __future__ import absolute_import, unicode_literals

from celery import shared_task

from src.customers.models import Offer, Customer
from .models import ShowroomCustomerSale, ShowroomCarsForSale
from ..dealer.models import Discount


@shared_task()
def buy_cars_for_customer():
    customers = Customer.objects.all()
    for customer in customers:
        offers = Offer.objects.filter(customer=customer, is_active=True)
        for offer in offers:
            cars = ShowroomCarsForSale.objects.filter(car__car__car=offer.car, is_active=True)
            d = {}
            for car in cars:
                try:
                    discount = Discount.objects.get(showroom=car.showroom).discount
                except Discount.DoesNotExist:
                    discount = 0
                car_price = car.price - (car.price * discount / 100)
                if car.car.car.car.pk in d:
                    if d[car.car.car.car.pk].get('price') > car_price:
                        d[car.car.car.car.pk] = {
                            'price': car_price,
                            'car_for_sale_pk': car.pk
                        }
                else:
                    d[car.car.car.pk] = {
                        'price': car_price,
                        'car_for_sale_pk': car.pk
                    }
            s = [x.get('car_for_sale_pk') for x in d.values()]
            cars = ShowroomCarsForSale.objects.filter(pk__in=s)
            for car in cars:
                try:
                    discount = Discount.objects.get(showroom=car.showroom)
                except Discount.DoesNotExist:
                    discount = None
                price = car.price - (car.price * discount.discount / 100) if discount else car.price
                customer_purchase = ShowroomCustomerSale(car_showroom=car.showroom,
                                                         customer=customer,
                                                         car=car.car.car.car,
                                                         discount=discount,
                                                         price=price)
                customer_purchase.save()

                customer.balance = customer.balance - price
                customer.save()

                car.is_active = False
                car.save()

                offer.is_active = False
                offer.save()

    return 'complete'
