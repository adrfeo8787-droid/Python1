import requests
import pytest

BASE_URL = "https://api.thedogapi.com/v1/breeds"
API_KEY = "live_YApFWP26IEK1bWiwFguNUGg7VqBmGUbRIA0OM0JqyzMz2ydcrPrlwNGEzi4HHHmR"  # Replace with your actual key or leave as "" if not needed

HEADERS = {"x-api-key": API_KEY} if API_KEY else {}

# -------------------------
# ✅ GET Method Test
# -------------------------
def test_get_breeds_returns_200():
    response = requests.get(BASE_URL, headers=HEADERS)
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    assert isinstance(response.json(), list), "Expected JSON response to be a list"

# -------------------------
# ❌ POST Method Test (expected to fail on public Dog API)
# -------------------------
def test_post_breed_not_allowed():
    sample_breed = {
        "name": "TestBreed",
        "origin": "UnitTestLand",
        "temperament": "Happy, Testing",
        "life_span": "10 - 12 years"
    }

    response = requests.post(BASE_URL, headers=HEADERS, json=sample_breed)
    # Public Dog API will reject POST, usually with 403 or 405
    assert response.status_code in [403, 405], (
        f"Expected 403 or 405, got {response.status_code}"
    )

# -------------------------
# ❌ DELETE Method Test (expected to fail on public Dog API)
# -------------------------
def test_delete_breed_not_allowed():
    # Try to delete a breed ID (will not work on public API)
    fake_breed_id = "1234"
    delete_url = f"{BASE_URL}/{fake_breed_id}"

    response = requests.delete(delete_url, headers=HEADERS)
    # Expecting 403 or 405 on public API
    assert response.status_code in [403, 405, 404], (
        f"Expected 403/405/404, got {response.status_code}"
    )
