import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.services.user_service import get_all_users

def test_get_users_returns_200():
    """
    Testa se a requisição GET de usuários retorna status 200
    e contém a chave 'data' na resposta JSON.
    """
    response = get_all_users()

    print("\nStatus Code:", response.status_code)
    print("Response Headers:", response.headers)
    print("Response Body:", response.text)

    # Valida código de resposta HTTP
    assert response.status_code == 200

    # Valida que a resposta contém o campo 'data' (lista de usuários)
    assert "data" in response.json()

