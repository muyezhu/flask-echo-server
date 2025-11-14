import pytest
from calculator_app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Calculator' in rv.data

def test_calculate_addition(client):
    rv = client.post('/calculate', json={'expression': '1+1'})
    assert rv.status_code == 200
    assert rv.json['result'] == 2

def test_calculate_multiplication(client):
    rv = client.post('/calculate', json={'expression': '3*4'})
    assert rv.status_code == 200
    assert rv.json['result'] == 12

def test_calculate_invalid_char(client):
    rv = client.post('/calculate', json={'expression': '1+1; exit()'})
    assert rv.status_code == 400
    assert 'error' in rv.json

def test_calculate_division_by_zero(client):
    rv = client.post('/calculate', json={'expression': '1/0'})
    assert rv.status_code == 400
    assert 'error' in rv.json
