from src.main import *
from unittest.mock import patch

def test_root():
    result = root()
    yield result
    assert result == {"message": "Meu primeiro EndPoint!"}

def test_segundoendpoint():
    with patch('random.randint', return_value=123):
        result = segundoendpoint()
        yield result

    assert result == {"teste":True, "num_random": 123}

def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = create_estudante(estudante_teste)
    yield result
    assert estudante_teste == result

def test_update_estudante_negativo():
    result = update_estudante(-5)
    yield result
    assert not result

def test_update_estudante_positivo():
    result = update_estudante(10)
    yield result
    assert result

def test_delete_estudante_negativo():
    result = delete_estudante(-5)
    yield result
    assert not result

def test_delete_estudante_positivo():
    result = delete_estudante(1)
    yield result
    assert result
