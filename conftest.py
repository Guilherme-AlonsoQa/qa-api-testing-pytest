"""Pytest fixtures for API tests."""

import pytest

from api.api_client import APIClient
from config.config import BASE_URL, TIMEOUT


@pytest.fixture(scope="session")
def api_client() -> APIClient:
    return APIClient(base_url=BASE_URL, timeout=TIMEOUT)
