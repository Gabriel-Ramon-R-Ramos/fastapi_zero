from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app

client = TestClient(app)


def test_read_root():
    response = client.get('/')

    assert response.json() == {'mensagem': 'Olá Mundo!'}
    assert response.status_code == HTTPStatus.OK
