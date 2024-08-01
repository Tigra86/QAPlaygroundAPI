import requests
import pytest

BASE_URL = "https://release-gs.qa-playground.com/api/v1"
AUTH_HEADER = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ"
                     ".eyJpc3MiOiJodHRwczovL215a290cWJvY2t6dnphY2NjdWJ6LnN1cGFiYXNlLmNvL2F1dGgvdjEiL"
                     "CJzdWIiOiI5NGM3MjY4OS1kYjAyLTRkNDEtYjAwNi01YzkxNWRiNmM4MzUiLCJhdWQiOiJhdXRoZW"
                     "50aWNhdGVkIiwiZXhwIjoxNzIyOTk0NjgzLCJpYXQiOjE3MjIzOTQ2ODMsImVtYWlsIjoidGlncmE"
                     "uYXphcnlhbkBtZS5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6Imdp"
                     "dGh1YiIsInByb3ZpZGVycyI6WyJnaXRodWIiXX0sInVzZXJfbWV0YWRhdGEiOnsiYXZhdGFyX3Vyb"
                     "CI6Imh0dHBzOi8vYXZhdGFycy5naXRodWJ1c2VyY29udGVudC5jb20vdS8yNjg1MTg2P3Y9NCIsIm"
                     "VtYWlsIjoidGlncmEuYXphcnlhbkBtZS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uY"
                     "W1lIjoiVGlncmFuIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJUaWdyYW"
                     "4iLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6IlRpZ3JhODYiLCJ"
                     "wcm92aWRlcl9pZCI6IjI2ODUxODYiLCJzdWIiOiIyNjg1MTg2IiwidXNlcl9uYW1lIjoiVGlncmE4N"
                     "iJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6Im9"
                     "hdXRoIiwidGltZXN0YW1wIjoxNzIwNDU4OTg2fV0sInNlc3Npb25faWQiOiI5MDU5NGQ0MC1hZGI1L"
                     "TRkOTUtODRjNS0wOWIxYmEwZjFkZDIiLCJpc19hbm9ueW1vdXMiOmZhbHNlfQ.XYMshvaqT2wvG0EXi"
                     "ZQxjHPMaIKslAIHXh5ZXLrZJ2I"
}


def headers():
    return {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ"
                         ".eyJpc3MiOiJodHRwczovL215a290cWJvY2t6dnphY2NjdWJ6LnN1cGFiYXNlLmNvL2F1dGgvdjEiL"
                         "CJzdWIiOiI5NGM3MjY4OS1kYjAyLTRkNDEtYjAwNi01YzkxNWRiNmM4MzUiLCJhdWQiOiJhdXRoZW"
                         "50aWNhdGVkIiwiZXhwIjoxNzIyOTk0NjgzLCJpYXQiOjE3MjIzOTQ2ODMsImVtYWlsIjoidGlncmE"
                         "uYXphcnlhbkBtZS5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6Imdp"
                         "dGh1YiIsInByb3ZpZGVycyI6WyJnaXRodWIiXX0sInVzZXJfbWV0YWRhdGEiOnsiYXZhdGFyX3Vyb"
                         "CI6Imh0dHBzOi8vYXZhdGFycy5naXRodWJ1c2VyY29udGVudC5jb20vdS8yNjg1MTg2P3Y9NCIsIm"
                         "VtYWlsIjoidGlncmEuYXphcnlhbkBtZS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uY"
                         "W1lIjoiVGlncmFuIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJUaWdyYW"
                         "4iLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6IlRpZ3JhODYiLCJ"
                         "wcm92aWRlcl9pZCI6IjI2ODUxODYiLCJzdWIiOiIyNjg1MTg2IiwidXNlcl9uYW1lIjoiVGlncmE4N"
                         "iJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6Im9"
                         "hdXRoIiwidGltZXN0YW1wIjoxNzIwNDU4OTg2fV0sInNlc3Npb25faWQiOiI5MDU5NGQ0MC1hZGI1L"
                         "TRkOTUtODRjNS0wOWIxYmEwZjFkZDIiLCJpc19hbm9ueW1vdXMiOmZhbHNlfQ.XYMshvaqT2wvG0EXi"
                         "ZQxjHPMaIKslAIHXh5ZXLrZJ2I",
                         "X-Task-Id": "API-3"
    }


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    response = requests.post(f"{BASE_URL}/setup", headers=AUTH_HEADER)
    assert response.status_code == 205


def test_add_new_user():
    # Step 1: Prepare request payload
    payload = {
        "email": "newuser@example.com",
        "password": "Password123",
        "name": "New User",
        "nickname": "newuser"
    }

    # Step 2: Send POST request to create a new user
    response = requests.post(f"{BASE_URL}/users", headers=headers(), json=payload)
    assert response.status_code == 200
    response_data = response.json()

    # Step 3: Verify response fields
    assert response_data['email'] == payload['email']
    assert response_data['name'] == payload['name']
    assert response_data['nickname'] == payload['nickname']
    assert 'uuid' in response_data

    # Step 4: Validate that a new user was created and exists in the user list
    response = requests.get(f"{BASE_URL}/users", headers=headers())
    assert response.status_code == 200
    users = response.json()
    assert any(users['users'][i]['uuid'] == response_data['uuid'] for i in range(len(users['users']))), \
        "User is not found in user list"

    """
    The code on the line 47 is doing the same as the following for loop:
        for i in range(len(users['users'])):
            assert users['users'][i]['uuid'] == response_data['uuid'], "User is not found in user list"
    """

    # Step 5: Verify that user information is successfully returned by sending GET request with the user uuid
    response = requests.get(f"{BASE_URL}/users/{response_data['uuid']}", headers=headers())
    assert response.status_code == 200
    user_data = response.json()
    assert user_data['email'] == payload['email']
    assert user_data['name'] == payload['name']
    assert user_data['nickname'] == payload['nickname']
    assert user_data['uuid'] == response_data['uuid']
