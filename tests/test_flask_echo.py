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

def test_echo_twice(client):
    sample_data = {"message": "test_message", "value": 42}
    expected_response_data = {
        "echo_twice": {
            "first": sample_data,
            "second": sample_data
        }
    }
    response = client.post('/echo_twice', json=sample_data)
    assert response.status_code == 200
    assert response.get_json() == expected_response_data

