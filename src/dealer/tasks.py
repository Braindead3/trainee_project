from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import DealerShowroomSale, CarForSale, Car, Discount
from src.car_showroom.models import CarShowroom
from djmoney.money import Money
from django.db.models import Q


@shared_task()
def buy_cars_for_showroom():
    all_showrooms = CarShowroom.objects.all()
    for showroom in all_showrooms:
        if showroom.balance > Money(0, 'USD'):
            preferred_characteristics = {'year': showroom.preferred_characteristics.get('year', 0),
                                         'gearbox': showroom.preferred_characteristics.get('gearbox', 'any'),
                                         'engine_volume': showroom.preferred_characteristics.get('engine_volume', 0),
                                         'mileage': showroom.preferred_characteristics.get('mileage', 0),
                                         'color': showroom.preferred_characteristics.get('color', 'any'),
                                         }
            preferred_cars = Car.objects.filter(
                Q(color=preferred_characteristics['color']) |
                Q(gearbox=preferred_characteristics['gearbox']) |
                Q(engine_volume__gte=preferred_characteristics['engine_volume']) |
                Q(mileage__gte=preferred_characteristics['mileage']) |
                Q(year__gte=preferred_characteristics['year'])
            )
            preferred_cars_for_sale = CarForSale.objects.filter(car__in=preferred_cars).order_by('price')
            d = {}
            for car in preferred_cars_for_sale:
                try:
                    discount = Discount.objects.get(dealer=car.dealer).discount
                except Discount.DoesNotExist:
                    discount = 0
                car_price = car.price - (car.price * discount / 100)
                if car.car.pk in d:
                    if d[car.car.pk].get('price') > car_price:
                        d[car.car.pk] = {
                            'price': car_price,
                            'car_for_sale_pk': car.pk
                        }
                else:
                    d[car.car.pk] = {
                        'price': car_price,
                        'car_for_sale_pk': car.pk
                    }
            s = [x.get('car_for_sale_pk') for x in d.values()]
            pr_c = CarForSale.objects.filter(pk__in=s)
            for car in pr_c:
                try:
                    discount = Discount.objects.get(dealer=car.dealer)
                except Discount.DoesNotExist:
                    discount = None
                price = car.price - (car.price * discount.discount / 100) if discount else car.price
                new_sale = DealerShowroomSale(dealer=car.dealer,
                                              car_showroom=showroom,
                                              car=car,
                                              discount=discount,
                                              price=price)
                new_sale.save()

                showroom.balance = showroom.balance - price
                showroom.save()
    return 'complete'
