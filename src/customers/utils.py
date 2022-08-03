from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Sum
from rest_framework_simplejwt.tokens import AccessToken

from src.car_showroom.models import ShowroomCustomerSale


class Email:
    @staticmethod
    def send_email(user_email, subject, message):
        send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[user_email])


def get_user_by_token(token):
    access_token_obj = AccessToken(token)
    user_id = access_token_obj['user_id']
    user = User.objects.get(id=user_id)
    return user


def get_amount_of_money_spent(customer_id):
    customer_purchases = ShowroomCustomerSale.objects.filter(customer=customer_id)
    if customer_purchases:
        money_spend = customer_purchases.aggregate(Sum('price'))
        return money_spend
    return 'Customer does not exists'


def get_customer_cars(customer_id):
    sales = ShowroomCustomerSale.objects.filter(customer=customer_id)
    if sales:
        data = []
        for sale in sales:
            data.append({'name': sale.car.name,
                         'year': sale.car.year,
                         'gearbox': sale.car.gearbox,
                         'mileage': sale.car.mileage,
                         'color': sale.car.color})
        return data
    return 'Customer do not buying anything yet'
