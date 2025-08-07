import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://api.thedogapi.com/v1/breeds"

@pytest.fixture(scope="session")
def api_key():
    return "live_YApFWP26IEK1bWiwFguNUGg7VqBmGUbRIA0OM0JqyzMz2ydcrPrlwNGEzi4HHHmR"

@pytest.fixture(scope="session")
def headers(api_key):
    return {"x-api-key": api_key} if api_key else {}