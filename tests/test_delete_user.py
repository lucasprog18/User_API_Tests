import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.services.user_service import delete_user

def test_delete_user_returns_204():
    """
    Testa exclusão de usuário existente.
    Valida se a API retorna status 204 No Content.
    """
    user_id = 2  # ID fictício usado pela API
    response = delete_user(user_id)

    assert response.status_code == 204
