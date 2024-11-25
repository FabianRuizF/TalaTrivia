import pytest
import requests



@pytest.fixture(scope="function")
def base_url():
    port = "8000"
    url = "http://0.0.0.0"
    return f"{url}:{port}"

def test_create_trivia(base_url):
    endpoint = "user/create/"
    # Test data
    user_data = {
        "name" : "Don McTest",
        "email": "donmc@example.com",
        "password": "secure_password123"
    }

    # Send POST request
    print(f"{base_url}/{endpoint}")
    try:
        response = requests.post(f"{base_url}/{endpoint}", json=user_data)
        user_id = response.json()["user_id"]
    except Exception as e:
        pytest.skip("Not been able to create trivia, create user failed")


    endpoint = "question/create/"
    question_data = {
        "question": "What is the chemical symbol for gold?",
        "answer_1": "Au",
        "answer_2": "Ag",
        "answer_3": "Hg",
        "answer_4": "Pb",
        "correct_answer": 1,
        "difficulty": 2
    }


    #We try to create a question, if we can't, we skip the test as we cannot test the trivia creation
    try:
        response = requests.post(f"{base_url}/{endpoint}", json=question_data)
        question_id  = response.json()["question_id"]
    except Exception as e:
        pytest.skip("Not been able to create trivia, create question failed")



    endpoint = "trivia/create/"
    # Test data
    user_data = {
        "name" : "Trivia Test",
        "description": "This is a trivia for testing",
        "question_list_id": [question_id],
        "user_list_id": [user_id],
    }

    # Send POST request
    print(f"{base_url}/{endpoint}")
    response = requests.post(f"{base_url}/{endpoint}", json=user_data)

    # Check if the response is correct, and if it returns the email without the password in the response
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, response is: {response.json()}"
