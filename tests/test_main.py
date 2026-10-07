"""
Phase 2 — Automated Tests for the Calculator API
Using pytest + FastAPI TestClient
"""

import pytest
from fastapi.testclient import TestClient
from main import app

# Create a test client — simulates HTTP requests without running a real server
client = TestClient(app)


# -------------------------------------------------------------------
# 1. Root endpoint
# -------------------------------------------------------------------
def test_root():
    """GET / should return a message confirming the API is running."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Calculator API is running!"}


# -------------------------------------------------------------------
# 2. Health endpoint
# -------------------------------------------------------------------
def test_health():
    """GET /health should return healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


# -------------------------------------------------------------------
# 3. Addition
# -------------------------------------------------------------------
def test_add():
    """GET /add?a=10&b=5 should return 15."""
    response = client.get("/add?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 15.0}


def test_add_negative_numbers():
    """GET /add?a=-3&b=-7 should return -10."""
    response = client.get("/add?a=-3&b=-7")
    assert response.status_code == 200
    assert response.json() == {"result": -10.0}


# -------------------------------------------------------------------
# 4. Subtraction
# -------------------------------------------------------------------
def test_subtract():
    """GET /subtract?a=10&b=5 should return 5."""
    response = client.get("/subtract?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


# -------------------------------------------------------------------
# 5. Multiplication
# -------------------------------------------------------------------
def test_multiply():
    """GET /multiply?a=10&b=5 should return 50."""
    response = client.get("/multiply?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 50.0}


def test_multiply_by_zero():
    """GET /multiply?a=10&b=0 should return 0."""
    response = client.get("/multiply?a=10&b=0")
    assert response.status_code == 200
    assert response.json() == {"result": 0.0}


# -------------------------------------------------------------------
# 6. Division
# -------------------------------------------------------------------
def test_divide():
    """GET /divide?a=10&b=5 should return 2."""
    response = client.get("/divide?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}


# -------------------------------------------------------------------
# 7. Division by zero
# -------------------------------------------------------------------
def test_divide_by_zero():
    """GET /divide?a=10&b=0 should return HTTP 400 error."""
    response = client.get("/divide?a=10&b=0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Division by zero is not allowed."}
