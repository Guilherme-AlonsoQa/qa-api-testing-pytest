"""Reusable API client built with requests."""

from __future__ import annotations

from typing import Any, Dict, Optional

import requests


class APIClient:
    """Simple reusable API client for CRUD-style calls."""

    def __init__(self, base_url: str, timeout: int = 10) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.trust_env = False
        self.session.headers.update({"Content-Type": "application/json"})

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.request(
            method=method,
            url=url,
            params=params,
            json=json,
            timeout=self.timeout,
        )

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        return self._request("POST", endpoint, json=json)
