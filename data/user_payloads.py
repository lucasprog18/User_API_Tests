from faker import Faker

faker = Faker()

def generate_valid_user_payload():
    """
    Gera um payload válido com nome e cargo aleatórios para criação de usuário.
    """
    return {
        "name": faker.first_name(),
        "job": faker.job()
    }

def generate_invalid_user_payload():
    """
    Gera um payload inválido (vazio ou incompleto), útil para testes negativos.
    """
    return {}

def generate_update_payload():
    """
    Gera um payload válido para atualização de usuário (pode simular PATCH).

    Returns:
        dict: contém novos valores para nome e cargo.
    """
    return {
        "name": faker.first_name(),
        "job": faker.job()
    }