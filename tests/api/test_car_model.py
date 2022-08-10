import pytest
from src.dealer.models import Car


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name, year, gearbox, engine_volume, mileage, color',
    [
        ("test_car", 2020, 'automatic', 2.5, 500, "white"),
    ]
)
def test_create_car(client, name, year, gearbox, engine_volume, mileage, color):
    payload = dict(name=name, year=year, gearbox=gearbox, engine_volume=engine_volume, mileage=mileage,
                   color=color)

    response = client.post('/api/dealer/cars/', payload)

    data = response.data

    car = Car.objects.all().first()

    assert response.status_code == 201
    assert data['name'] == car.name
    assert data['year'] == car.year
    assert data['gearbox'] == car.gearbox
    assert data['engine_volume'] == car.engine_volume
    assert data['mileage'] == car.mileage
    assert data['color'] == car.color


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name, year, gearbox, engine_volume, mileage, color',
    [
        ("test_car", 2020, 'automatic', 2.5, 500, "white"),
    ]
)
def test_get_car_detail(client, car, name, year, gearbox, engine_volume, mileage, color):
    car = car(name=name, year=year, gearbox=gearbox, engine_volume=engine_volume, mileage=mileage,
              color=color)

    response = client.get('/api/dealer/cars/2/')

    data = response.data

    assert data['name'] == car.name
    assert data['year'] == car.year
    assert data['gearbox'] == car.gearbox
    assert data['engine_volume'] == car.engine_volume
    assert data['mileage'] == car.mileage
    assert data['color'] == car.color


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name, year, gearbox, engine_volume, mileage, color',
    [
        ("test_car", 2020, 'automatic', 2.5, 500, "white"),
    ]
)
def test_car_update(client, car, name, year, gearbox, engine_volume, mileage, color):
    car = car(name=name, year=year, gearbox=gearbox, engine_volume=engine_volume, mileage=mileage,
              color=color)

    payload = {'name': 'update test_car'}

    response = client.patch(f'/api/dealer/cars/{car.pk}/', payload)

    car.refresh_from_db()

    assert response.status_code == 200
    assert car.name == payload['name']


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name, year, gearbox, engine_volume, mileage, color',
    [
        ("test_car", 2020, 'automatic', 2.5, 500, "white"),
    ]
)
def test_car_delete(client, car, name, year, gearbox, engine_volume, mileage, color):
    car = car(name=name, year=year, gearbox=gearbox, engine_volume=engine_volume, mileage=mileage,
              color=color)

    response = client.delete(f'/api/dealer/cars/{car.pk}/')

    assert response.status_code == 204

    with pytest.raises(Car.DoesNotExist):
        car.refresh_from_db()
