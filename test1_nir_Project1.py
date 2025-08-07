import pytest

def test_get_breeds_returns_200(base_url, headers):
    response = requests.get(base_url, headers=headers)
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    assert isinstance(response.json(), list), "Expected JSON response to be a list"
    print("\n✅ Status code is 200 OK.")

@pytest.mark.skip(reason="Public API does not allow POST")
def test_post_breed_not_allowed(base_url, headers):
    sample_breed = {
        "name": "TestBreed",
        "origin": "UnitTestLand",
        "temperament": "Happy, Testing",
        "life_span": "10 - 12 years"
    }

    response = requests.post(base_url, headers=headers, json=sample_breed)
    assert response.status_code in [403, 405], f"Expected 403 or 405, got {response.status_code}"

@pytest.mark.skip(reason="Public API does not allow DELETE")
def test_delete_breed_not_allowed(base_url, headers):
    fake_breed_id = "1234"
    delete_url = f"{base_url}/{fake_breed_id}"
    response = requests.delete(delete_url, headers=headers)
    assert response.status_code in [403, 405, 404], f"Expected 403/405/404, got {response.status_code}"