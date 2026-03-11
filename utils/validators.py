"""Reusable validation helpers for API response assertions."""

from __future__ import annotations

from typing import Iterable, Mapping


def assert_status_code(actual: int, expected: int) -> None:
    assert actual == expected, f"Expected status code {expected}, got {actual}"


def assert_json_list(data: object) -> None:
    assert isinstance(data, list), f"Expected response JSON to be a list, got {type(data).__name__}"


def assert_required_fields(item: Mapping[str, object], required_fields: Iterable[str]) -> None:
    missing = [field for field in required_fields if field not in item]
    assert not missing, f"Missing required fields: {missing}"
