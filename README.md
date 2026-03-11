# QA API Testing Framework (Pytest + Requests)

A clean and reusable API testing framework built for QA automation portfolio use.  
This project validates core REST API behavior against the public JSONPlaceholder API:
https://jsonplaceholder.typicode.com

## API Testing Concept

API testing verifies the behavior, reliability, and contract of backend services without relying on a UI.
In this project, tests focus on:

- **Status code validation** (e.g., 200 OK, 201 Created)
- **Response field validation** (required keys are present)
- **JSON structure validation** (list/object structure and nested types)

This ensures endpoints return predictable and correct results for both read and create operations.

## Tools Used

- **Python** – programming language
- **Pytest** – test framework and fixtures
- **Requests** – HTTP client library
- **GitHub Actions** – CI pipeline automation

## Project Structure

```text
qa-api-testing-pytest/
│
├── tests/
│   ├── test_users.py
│   └── test_posts.py
│
├── api/
│   └── api_client.py
│
├── data/
│   └── payloads.py
│
├── utils/
│   └── validators.py
│
├── config/
│   └── config.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .github/workflows/tests.yml
```

## Endpoints Covered

- `GET /users`
- `GET /posts`
- `POST /posts`

## How to Run Tests

### 1) Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run the test suite

```bash
pytest
```

## Configuration

Environment variables (optional):

- `BASE_URL` (default: `https://jsonplaceholder.typicode.com`)
- `API_TIMEOUT` (default: `10` seconds)

Example:

```bash
BASE_URL=https://jsonplaceholder.typicode.com API_TIMEOUT=15 pytest
```

## CI Pipeline

GitHub Actions workflow: **`.github/workflows/tests.yml`**

The pipeline automatically:

1. Checks out the repository
2. Sets up Python 3.11
3. Installs dependencies from `requirements.txt`
4. Runs `pytest`

This provides continuous validation for every push and pull request.

## Portfolio Value

This project demonstrates:

- reusable API client design
- fixture-based test architecture
- clear assertion utilities for maintainable tests
- CI-ready QA automation practices

It is intentionally structured for readability, scalability, and professional presentation in a QA automation portfolio.
