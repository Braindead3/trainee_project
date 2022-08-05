import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from src.dealer.models import Dealer


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
