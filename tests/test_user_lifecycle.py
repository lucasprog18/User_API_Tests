import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.services.user_service import create_user, update_user, delete_user
from data.user_payloads import generate_valid_user_payload, generate_update_payload
from schemas.user_schemas import CreatedUserResponse, UpdatedUserResponse

def test_user_full_lifecycle():
    # CREATE
    payload_create = generate_valid_user_payload()
    response_create = create_user(payload_create)
    assert response_create.status_code == 201

    body_create = response_create.json()
    CreatedUserResponse(**body_create)  # valida estrutura
    user_id = body_create.get("id")

    # UPDATE
    payload_update = generate_update_payload()
    response_update = update_user(user_id, payload_update)
    assert response_update.status_code == 200
    UpdatedUserResponse(**response_update.json())

    # DELETE
    response_delete = delete_user(user_id)
    assert response_delete.status_code == 204
