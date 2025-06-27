import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from src.services.user_service import create_user, update_user, delete_user
from data.user_payloads import generate_invalid_user_payload

def test_post_user_with_empty_payload_returns_201():
    """
    Reqres API (mock) allows creating users with empty payloads.
    This test confirms that the endpoint returns 201 regardless of body.
    """
    payload = generate_invalid_user_payload()
    response = create_user(payload)

    assert response.status_code == 201
    body = response.json()
    assert "id" in body
    assert "createdAt" in body

def test_put_user_with_nonexistent_id_still_returns_200():
    """
    Reqres API accepts any user ID for PUT requests.
    This test uses an unlikely ID and verifies the mock still returns 200 OK.
    """
    nonexistent_id = 9999
    payload = {"name": "Ghost", "job": "Phantom"}
    response = update_user(nonexistent_id, payload)

    assert response.status_code == 200
    assert "updatedAt" in response.json()

def test_delete_user_with_nonexistent_id_returns_204():
    """
    Reqres API always returns 204 No Content for DELETE, even if ID does not exist.
    This test documents that behavior.
    """
    nonexistent_id = 9999
    response = delete_user(nonexistent_id)

    assert response.status_code == 204
