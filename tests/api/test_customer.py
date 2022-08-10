import pytest


@pytest.mark.django_db
def test_register_user(client):
    payload = {
        'username': 'register_test',
        'email': 'register_test@gmail.com',
        'password': 'vl1357chd9753',
        'password2': 'vl1357chd9753'
    }

    response = client.post('/api/customers/user/register_new_user/', payload)

    data = response.data

    assert data['username'] == payload['username']
    assert data['email'] == payload['email']
    assert 'password' not in data


@pytest.mark.django_db
def test_login_user(user, client):
    response = client.post('/api/token/', dict(username='fixture_user', password='vl1357chd9753'))

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail(client):
    response = client.post('/api/token/', dict(username='register_test', password='vl1357chd9753'))

    assert response.status_code == 401
