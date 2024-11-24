import pytest
import requests



@pytest.fixture(scope="function")
def base_url():
    port = "8000"
    url = "http://0.0.0.0"
    return f"{url}:{port}"


def test_create_question(base_url):
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
    response = requests.post(f"{base_url}/{endpoint}", json=question_data)

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, response is: {response.json()}"
    assert response.json()["answer_1"] == question_data["answer_1"]
    #We correctly created our question, now we will clean it, if it fails, the test should not fail because we are only testing creation
    try:
        endpoint = "question/delete/"
        response = requests.delete(f"{base_url}/{endpoint}", json=question_data)
    except Exception as e:
        print(f"Something happen on test_create while deleting: {e}")
        pass

def test_delete_question(base_url):
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


    #We try to create a question, if we can't, we skip the test as we cannot test the delete
    try:
        response = requests.post(f"{base_url}/{endpoint}", json=question_data)
        question_data = {
            "question_id": response.json()["question_id"],
        }
    except Exception as e:
        pytest.skip("Not been able to create question")

    endpoint = "question/delete/"

    # Send DELETE request
    print(f"{base_url}/{endpoint}")
    response = requests.delete(f"{base_url}/{endpoint}", json=question_data)
    # Check if the response is correct
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, response is: {response.json()}"
