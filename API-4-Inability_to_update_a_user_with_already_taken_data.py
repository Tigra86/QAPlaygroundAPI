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
        "X-Task-Id": "API-4"
    }


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    response = requests.post(f"{BASE_URL}/setup", headers=AUTH_HEADER)
    assert response.status_code == 205


def test_inability_to_update_a_user_with_already_taken_data():
    # Step 1: Get user list
    response = requests.get(f"{BASE_URL}/users", headers=headers())
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 0, "No users found"

    # Step 2: Choose a first user and get user email
    user_1_email = users['users'][0]['email']

    # Step 3: Choose a second user and get user uuid
    user_2_uuid = users['users'][1]['uuid']

    # Step 4: Send PATCH request to try to update a user with already taken data
    response = requests.patch(
        url=f"{BASE_URL}/users/{user_2_uuid}",
        headers=headers(),
        json={
            "email": user_1_email
    })
    assert response.status_code == 409

    # Step 5: Validate that correct message is presented
    message = response.json()['message']
    assert message == f'User with the following "email" already exists: {user_1_email}', 'Wrong message is presented'
