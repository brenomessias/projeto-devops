import requests

def consultar_cotacao(nome_da_moeda: str) -> None:
    # Vai até a API pública da coinbase e pergunta qual é o preço atual da cripto escolhida
    endereco_api = f"https://api.coinbase.com/v2/prices/{nome_da_moeda}/spot"

    try:
        # É como se estivéssemos abrindo uma aba no navegador e acessando o site
        resposta_do_servidor = requests.get(endereco_api)

        #  O código 200 significa "sucesso"
        if resposta_do_servidor.status_code == 200:

            # O formato JSON é entendido como um dicionário em python
            dados_recebidos = resposta_do_servidor.json()

            # Busca o preço exato navegando nas chaves do dicionário
            preco_em_reais = float(dados_recebidos['data']['amount'])

            # Formatando o texto para exibir  no terminal do pycharm
            print(f">> O preço atual de {nome_da_moeda.capitalize()} é de R$ {preco_em_reais:,.2f}")

        else:
            print(f"O servidor retornou um erro. Código do erro: {resposta_do_servidor.status_code}")

    except Exception as erro:
        # Se a internet cair, o site estiver fora do ar ou o pacote requests falhar, caímos aqui
        print(f"Problema de conexão ao tentar buscar o preço. Mais detalhes: {erro}")


# Ao dar play, o código começa por aqui
if __name__ == "__main__":
    print("Monitorando as criptos...\n")

    # Testes com algumas criptos
    consultar_cotacao("BTC-BRL")
    consultar_cotacao("ETH-BRL")
    consultar_cotacao("SOL-BRL")