"""Tests for /users endpoint."""

from utils.validators import assert_json_list, assert_required_fields, assert_status_code


def test_get_users_returns_expected_structure(api_client):
    response = api_client.get("/users")

    assert_status_code(response.status_code, 200)
    data = response.json()
    assert_json_list(data)
    assert len(data) > 0, "Expected at least one user in response"

    first_user = data[0]
    assert_required_fields(first_user, ["id", "name", "username", "email", "address", "company"])
    assert isinstance(first_user["address"], dict), "Expected 'address' to be a dictionary"
    assert isinstance(first_user["company"], dict), "Expected 'company' to be a dictionary"
