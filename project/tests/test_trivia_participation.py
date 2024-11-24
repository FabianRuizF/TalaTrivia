import pytest
import requests



@pytest.fixture(scope="function")
def base_url():
    port = "8000"
    url = "http://0.0.0.0"
    return f"{url}:{port}"

def test_list_question_from_trivia(base_url):
    endpoint = "trivia_participation/read/"
    # Test data
    trivia_data = {
        "trivia_id" : "1"
    }

    # Send POST request
    print(f"{base_url}/{endpoint}")
    response = requests.post(f"{base_url}/{endpoint}", json=trivia_data)

    # Check if the response is correct, and if it returns the email without the password in the response
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, response is: {response.json()}"
    assert "question_list" in response.json()
    assert "question" not in response.json()["question_list"][0]
    assert "correct_answer" not in response.json()
