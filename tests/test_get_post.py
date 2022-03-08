# Third party modules
import pytest

# First party modules
from http_app.app import init_app


@pytest.fixture
def client():
    app = init_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_simple_get(client):
    rv = client.get("/")
    assert b"<p>Hello, World</p>" == rv.data

def test_json_get(client):
    rv = client.get("/",headers={"Accept": "application/json"})
    assert b'{"message":"Hello, World"}\n' == rv.data

def test_simple_post(client):
    rv = client.post("/")
    assert b"<p>Hello, World</p>" == rv.data

def test_json_post(client):
    rv = client.post("/",headers={"Accept": "application/json"})
    assert b'<p>Hello, World</p>' == rv.data
