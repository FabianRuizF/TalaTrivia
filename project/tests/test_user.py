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
        "name" : "Test McTest",
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


def test_delete_user(base_url):
    endpoint = "user/delete/"

    # Test data
    user_email = "test@example.com"
    user_data = {
        "email": user_email,
    }

    # Send DELETE request
    print(f"{base_url}/{endpoint}")
    response = requests.delete(f"{base_url}/{endpoint}", json=user_data)

    # Check if the response is correct
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

