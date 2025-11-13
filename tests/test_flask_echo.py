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

def test_add_success(client):
    response = client.post('/add', json={"numbers": [1, 2, 3]})
    assert response.status_code == 200
    assert response.get_json() == {"sum": 6}

def test_add_invalid_input(client):
    response = client.post('/add', json={"nums": [1, 2, 3]})
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_add_non_numeric_input(client):
    response = client.post('/add', json={"numbers": [1, "a", 3]})
    assert response.status_code == 400
    assert "error" in response.get_json()
