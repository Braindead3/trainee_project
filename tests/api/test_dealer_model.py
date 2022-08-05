import pytest
from src.dealer.models import Dealer


@pytest.mark.django_db
def test_create_dealer(client):
    payload = {
        "name": "test_dealer",
        "year": 2020,
        "customers_amount": 10,
        "description": "Test dealer",
        "country": "AF"
    }

    response = client.post('/api/dealer/dealers/', payload)

    data = response.data

    dealer_from_db = Dealer.objects.all().first()

    assert data['name'] == dealer_from_db.name
    assert data['year'] == dealer_from_db.year
    assert data['customers_amount'] == dealer_from_db.customers_amount
    assert data['description'] == dealer_from_db.description
    assert data['country'] == dealer_from_db.country


@pytest.mark.django_db
def test_get_all_dealers(client):
    Dealer.objects.create(name="test_dealer",
                          year=2020,
                          customers_amount=10,
                          description="Test dealer",
                          country="AF")
    Dealer.objects.create(name="test_dealer2",
                          year=2021,
                          customers_amount=0,
                          description="Test dealer 2",
                          country="AF")

    response = client.get('/api/dealer/dealers/')

    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_get_dealer_detail_404(client):
    response = client.get('/api/dealer/dealers/0/')

    assert response.status_code == 404


@pytest.mark.django_db
def test_get_dealer_detail(client, dealer):
    response = client.get('/api/dealer/dealers/4/')

    data = response.data

    dealer_from_db = Dealer.objects.all().first()

    assert response.status_code == 200
    assert data['name'] == dealer_from_db.name
    assert data['year'] == dealer_from_db.year
    assert data['customers_amount'] == dealer_from_db.customers_amount
    assert data['description'] == dealer_from_db.description
    assert data['country'] == dealer_from_db.country


@pytest.mark.django_db
def test_dealer_update(client, dealer):
    payload = {'name': 'update test_dealer'}

    response = client.patch(f'/api/dealer/dealers/{dealer.pk}/', payload)

    dealer.refresh_from_db()

    assert response.status_code == 200
    assert dealer.name == payload['name']


@pytest.mark.django_db
def test_dealer_delete(client, dealer):
    response = client.delete(f'/api/dealer/dealers/{dealer.pk}/')

    assert response.status_code == 204

    with pytest.raises(Dealer.DoesNotExist):
        dealer.refresh_from_db()
