import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_profile_requires_auth():
    """Test that getting profile requires authentication"""
    response = client.get("/users/me")
    assert response.status_code == 401

def test_update_profile_requires_auth():
    """Test that updating profile requires authentication"""
    response = client.put("/users/me", json={"first_name": "Test"})
    assert response.status_code == 401

def test_change_password_requires_auth():
    """Test that changing password requires authentication"""
    response = client.put("/users/me/password", json={
        "current_password": "old",
        "new_password": "new",
        "confirm_new_password": "new"
    })
    assert response.status_code == 401

def test_profile_page_loads():
    """Test that profile page loads"""
    response = client.get("/profile")
    assert response.status_code == 200
    assert b"Profile" in response.content
