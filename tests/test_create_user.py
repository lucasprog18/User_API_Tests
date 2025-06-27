import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.services.user_service import create_user
from data.user_payloads import generate_valid_user_payload, generate_invalid_user_payload
from schemas.user_schemas import CreatedUserResponse

def test_create_user_success():
    """
    Testa criação de usuário com payload válido.
    Valida status 201 e presença dos campos 'id' e 'createdAt' na resposta.
    """
    payload = generate_valid_user_payload()
    response = create_user(payload)

    assert response.status_code == 201
    CreatedUserResponse(**response.json())  # valida o schema
    body = response.json()
    assert "id" in body
    assert "createdAt" in body
    

def test_create_user_with_empty_payload_should_return_201_even_if_empty():
    """
    Reqres.in aceita payloads vazios no POST /users.
    Esse teste confirma esse comportamento da API.
    """
    payload = generate_invalid_user_payload()
    response = create_user(payload)

    assert response.status_code == 201
    assert "id" in response.json()


