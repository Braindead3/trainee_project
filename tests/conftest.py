import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from src.dealer.models import Dealer, Car


@pytest.fixture
def user():
    user = User(username='fixture_user', email='fixture@gmail.com')
    user.set_password('vl1357chd9753')
    user.save()

    return user


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def dealer():
    return Dealer.objects.create(name="test_dealer",
                                 year=2020,
                                 customers_amount=10,
                                 description="Test dealer",
                                 country="AF")


@pytest.fixture
def car(**kwargs):
    def create_car(**kwargs):
        name = kwargs.pop('name')
        year = kwargs.pop('year')
        gearbox = kwargs.pop('gearbox')
        engine_volume = kwargs.pop('engine_volume')
        mileage = kwargs.pop('mileage')
        color = kwargs.pop('color')
        car = Car.objects.create(name=name,
                                 year=year,
                                 gearbox=gearbox,
                                 engine_volume=engine_volume,
                                 mileage=mileage,
                                 color=color)
        return car

    return create_car
