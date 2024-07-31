import requests
import pytest

BASE_URL = "https://release-gs.qa-playground.com/api/v1"
AUTH_HEADER = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL215a290cWJvY2t6dnphY2NjdWJ6LnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiI5NGM3MjY4OS1kYjAyLTRkNDEtYjAwNi01YzkxNWRiNmM4MzUiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzIyOTk0NjgzLCJpYXQiOjE3MjIzOTQ2ODMsImVtYWlsIjoidGlncmEuYXphcnlhbkBtZS5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6ImdpdGh1YiIsInByb3ZpZGVycyI6WyJnaXRodWIiXX0sInVzZXJfbWV0YWRhdGEiOnsiYXZhdGFyX3VybCI6Imh0dHBzOi8vYXZhdGFycy5naXRodWJ1c2VyY29udGVudC5jb20vdS8yNjg1MTg2P3Y9NCIsImVtYWlsIjoidGlncmEuYXphcnlhbkBtZS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiVGlncmFuIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJUaWdyYW4iLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6IlRpZ3JhODYiLCJwcm92aWRlcl9pZCI6IjI2ODUxODYiLCJzdWIiOiIyNjg1MTg2IiwidXNlcl9uYW1lIjoiVGlncmE4NiJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6Im9hdXRoIiwidGltZXN0YW1wIjoxNzIwNDU4OTg2fV0sInNlc3Npb25faWQiOiI5MDU5NGQ0MC1hZGI1LTRkOTUtODRjNS0wOWIxYmEwZjFkZDIiLCJpc19hbm9ueW1vdXMiOmZhbHNlfQ.XYMshvaqT2wvG0EXiZQxjHPMaIKslAIHXh5ZXLrZJ2I"
}


def headers():
    return {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL215a290cWJvY2t6dnphY2NjdWJ6LnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiI5NGM3MjY4OS1kYjAyLTRkNDEtYjAwNi01YzkxNWRiNmM4MzUiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzIyOTk0NjgzLCJpYXQiOjE3MjIzOTQ2ODMsImVtYWlsIjoidGlncmEuYXphcnlhbkBtZS5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6ImdpdGh1YiIsInByb3ZpZGVycyI6WyJnaXRodWIiXX0sInVzZXJfbWV0YWRhdGEiOnsiYXZhdGFyX3VybCI6Imh0dHBzOi8vYXZhdGFycy5naXRodWJ1c2VyY29udGVudC5jb20vdS8yNjg1MTg2P3Y9NCIsImVtYWlsIjoidGlncmEuYXphcnlhbkBtZS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiVGlncmFuIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJUaWdyYW4iLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6IlRpZ3JhODYiLCJwcm92aWRlcl9pZCI6IjI2ODUxODYiLCJzdWIiOiIyNjg1MTg2IiwidXNlcl9uYW1lIjoiVGlncmE4NiJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6Im9hdXRoIiwidGltZXN0YW1wIjoxNzIwNDU4OTg2fV0sInNlc3Npb25faWQiOiI5MDU5NGQ0MC1hZGI1LTRkOTUtODRjNS0wOWIxYmEwZjFkZDIiLCJpc19hbm9ueW1vdXMiOmZhbHNlfQ.XYMshvaqT2wvG0EXiZQxjHPMaIKslAIHXh5ZXLrZJ2I",
        "X-Task-Id": "API-2"
    }


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    response = requests.post(f"{BASE_URL}/setup", headers=AUTH_HEADER)
    assert response.status_code == 205


def test_search_games_by_keyword():
    # Step 1: Get list of all games
    response = requests.get(f"{BASE_URL}/games", headers=headers())
    assert response.status_code == 200
    games = response.json()
    assert len(games) > 0, "No games found"

    # Step 2: Choose a game and get part of its name
    game_name_part = games['games'][0]['title'].split()[0]

    # Step 3: Prepare the search query param
    params = {
        "query": game_name_part
    }

    # Step 4: Send GET request to search games by keyword
    response = requests.get(f"{BASE_URL}/games/search", headers=headers(), params=params)
    assert response.status_code == 200

    # Step 5: Verify the response payload
    search_results = response.json()
    assert 'games' in search_results
    assert 'meta' in search_results
    assert isinstance(search_results['games'], list)

    for game in search_results['games']:
        assert 'uuid' in game
        assert 'title' in game
        assert 'category_uuids' in game
        assert 'price' in game
        assert game_name_part.lower() in game['title'].lower()
