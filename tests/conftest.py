import pytest
from faker import Faker

@pytest.fixture(scope="function")
def fake():
    """
    Fixture global para geração de dados dinâmicos com faker.
    """
    return Faker()
