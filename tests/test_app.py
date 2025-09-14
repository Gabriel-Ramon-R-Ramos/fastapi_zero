from http import HTTPStatus


def test_read_root(client):
    response = client.get('/')

    assert response.json() == {'message': 'Olá Mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'alice@example.com',
        'username': 'alice',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'alice',
                'email': 'alice@example.com',
            }
        ]
    }


def test_read_only_users(client):
    response = client.get('/users/1')
    response_error = client.get('/users/-1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }

    assert response_error.status_code == HTTPStatus.NOT_FOUND
    assert response_error.json() == {'detail': 'User not found!'}


def test_update_user(client):
    response = client.put(
        'users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    response_error = client.put(
        'users/-1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }

    assert response_error.status_code == HTTPStatus.NOT_FOUND
    assert response_error.json() == {'detail': 'User not found!'}


def test_delete_user(client):
    response = client.delete('/users/1')
    response_error = client.delete('users/-1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }

    assert response_error.status_code == HTTPStatus.NOT_FOUND
    assert response_error.json() == {'detail': 'User not found!'}
