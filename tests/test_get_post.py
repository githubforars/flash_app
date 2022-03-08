# Third party modules
import pytest

# First party modules
from http_app.app import init_app


@pytest.fixture
def client():
    app = init_app()
    with app.test_client() as client:
        yield client


def test_simple_get(client):
    res = client.get("/")
    assert b"<p>Hello, World</p>" == res.data

def test_json_get(client):
    res = client.get("/",headers={"Accept": "application/json"})
    assert b'{"message":"Hello, World"}\n' == res.data

def test_simple_post(client):
    res = client.post("/")
    assert b"<p>Hello, World</p>" == res.data

def test_json_post(client):
    res = client.post("/",headers={"Accept": "application/json"})
    assert b'<p>Hello, World</p>' == res.data

def test_put(client):
    res = client.put("/")
    assert res.status_code == 405
