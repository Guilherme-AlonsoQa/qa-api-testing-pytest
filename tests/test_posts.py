"""Tests for /posts endpoint."""

from data.payloads import NEW_POST_PAYLOAD
from utils.validators import assert_json_list, assert_required_fields, assert_status_code


def test_get_posts_returns_expected_structure(api_client):
    response = api_client.get("/posts")

    assert_status_code(response.status_code, 200)
    data = response.json()
    assert_json_list(data)
    assert len(data) > 0, "Expected at least one post in response"

    first_post = data[0]
    assert_required_fields(first_post, ["userId", "id", "title", "body"])


def test_create_post_returns_created_resource(api_client):
    response = api_client.post("/posts", json=NEW_POST_PAYLOAD)

    assert_status_code(response.status_code, 201)
    data = response.json()
    assert_required_fields(data, ["title", "body", "userId", "id"])

    assert data["title"] == NEW_POST_PAYLOAD["title"]
    assert data["body"] == NEW_POST_PAYLOAD["body"]
    assert data["userId"] == NEW_POST_PAYLOAD["userId"]
