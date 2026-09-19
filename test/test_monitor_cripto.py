import token
from unittest.mock import patch, MagicMock

import pytest

from src.monitor_cripto import consultar_cotacao


@pytest.mark.parametrize("token", ["BTC-BRL"])
def test_consultar_cotacao_sucesso(capsys, token):
    resposta_simulada = MagicMock()
    resposta_simulada.status_code = 200
    resposta_simulada.json.return_value = {"data": {"amount": "148.32"}}

    with patch("src.monitor_cripto.requests.get", return_value=resposta_simulada) as mock_get:
        consultar_cotacao(token)

    # Garante que a Url foi montada corretamente com o token pedido
    mock_get.assert_called_once_with(
        f"https://api.coinbase.com/v2/prices/{token}/spot"
    )

    result = capsys.readouterr().out
    assert "Btc-brl" in result
    assert "148.32" in result


def test_consultar_cotacao_erro(capsys):
    resposta_simulada = MagicMock()
    resposta_simulada.status_code = 500

    with patch("src.monitor_cripto.requests.get", return_value=resposta_simulada):
        consultar_cotacao("ETH-BRL")

    result = capsys.readouterr().out
    assert "erro" in result.lower()
    assert "500" in result


def test_consultar_cotacao_falha_conexao(capsys):
    # Simula uma falha de conexao
    with patch("src.monitor_cripto.requests.get", side_effect=ConnectionError("Falha simulada de rede")):
        consultar_cotacao("SOL-BRL")

    result = capsys.readouterr().out
    assert "Problema de conexão" in result
    assert "Falha simulada de rede" in result