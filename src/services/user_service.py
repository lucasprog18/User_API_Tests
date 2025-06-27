import requests
import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()



# URL base da API utilizada
BASE_URL = "https://reqres.in/api"

# Chave de autenticação exigida pela API
API_KEY = os.getenv("REQRES_API_KEY")

# Cabeçalho exigido pela API
HEADERS = {
    "x-api-key": API_KEY
}

def get_all_users(page=1):
    """
    Envia uma requisição GET autenticada para listar usuários da API.

    Args:
        page (int): número da página que será consultada.

    Returns:
        Response: objeto response do requests contendo status e corpo da resposta.
    """
    url = f"{BASE_URL}/users"
    response = requests.get(url, headers=HEADERS, params={"page": page})
    return response

def create_user(payload):
    """
    Envia uma requisição POST autenticada para criar um novo usuário.

    Args:
        payload (dict): corpo da requisição com 'name' e 'job'.

    Returns:
        Response: resposta HTTP com status, ID e data de criação.
    """
    url = f"{BASE_URL}/users"
    return requests.post(url, headers=HEADERS, json=payload)

def update_user(user_id, payload):
    """
    Envia uma requisição PUT autenticada para atualizar um usuário específico.

    Args:
        user_id (int or str): ID do usuário a ser atualizado.
        payload (dict): dados com campos a atualizar, como 'name' ou 'job'.

    Returns:
        Response: resposta HTTP contendo status e campo 'updatedAt'.
    """
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.put(url, headers=HEADERS, json=payload)
    return response

def delete_user(user_id):
    """
    Envia uma requisição DELETE autenticada para remover um usuário.

    Args:
        user_id (int or str): ID do usuário a ser deletado.

    Returns:
        Response: resposta HTTP (esperado 204 No Content).
    """
    url = f"{BASE_URL}/users/{user_id}"
    return requests.delete(url, headers=HEADERS)
