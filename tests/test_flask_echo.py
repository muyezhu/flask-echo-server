import pytest
from flask_echo_server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_echo(client):
    response = client.post('/echo', json={"message": "Hello, World!"})
    assert response.status_code == 200
    assert response.get_json() == {"echo": {"message": "Hello, World!"}}


def test_xyz(client):
    response = client.get('/echo_xyz')
    assert response.status_code == 200
    assert response.get_json() == {"xyz": "xyz"}

