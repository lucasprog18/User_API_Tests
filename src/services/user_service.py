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
