from src.main import *
from unittest.mock import patch

import pytest

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Meu primeiro EndPoint!"}


@pytest.mark.asyncio
async def test_segundoendpoint():
    with patch('random.randint', return_value=123):
        result = await segundoendpoint()
    assert result == {"teste":True, "num_random": 123}

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result


@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result


@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result


@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result


@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(1)
    assert result
