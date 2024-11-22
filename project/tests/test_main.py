import pytest
import requests

port = "8000"
url = "http://0.0.0.0"
base_url = f"{url}:{port}"


@pytest.fixture(scope="function")
def base_url():
    port = "8000"
    url = "http://0.0.0.0"
    return f"{url}:{port}"

def test_read_root(base_url):
    endpoint = "/"
    response = requests.get(base_url+endpoint)
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
