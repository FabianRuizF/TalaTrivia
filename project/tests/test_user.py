import pytest
import requests



@pytest.fixture(scope="function")
def base_url():
    port = "8000"
    url = "http://0.0.0.0"
    return f"{url}:{port}"

def test_create_user(base_url):
    endpoint = "user/create/"

    # Test data
    user_data = {
        "email": "test@example.com",
        "password": "secure_password123"
    }

    # Send POST request
    print(f"{base_url}/{endpoint}")
    response = requests.post(f"{base_url}/{endpoint}", json=user_data)

    # Check if the response is correct, and if it returns the email without the password in the response
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]
    assert "password" not in response.json()
