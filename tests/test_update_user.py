import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.services.user_service import update_user
from data.user_payloads import generate_update_payload

def test_update_user_returns_200_and_updatedAt():
    """
    Testa atualização de usuário via PUT.
    Verifica se o status é 200 e se a resposta contém o campo 'updatedAt'.
    """
    user_id = 2  # user ID conhecido e fixo da API Reqres
    payload = generate_update_payload()

    response = update_user(user_id, payload)

    assert response.status_code == 200
    body = response.json()
    assert "updatedAt" in body
