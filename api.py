#type:ignore

import requests

def cambios(moeda_local: str = "BRL"):
    url = f'https://open.er-api.com/v6/latest/{moeda_local}'
    try:
        reposta = requests.get(url)
        reposta.raise_for_status()
        dados= reposta.json()
        return dados
    except requests.exceptions.RequestException as erro:
        print(f'Erro ao conectar na API: {erro}')
        return 
    except ValueError as erro:
        prin(f'Erro ao fazer o Json: {erro}')   
        return
    
if __name__ == "__main__":
    dados_moeda = cambios()

    if dados_moeda:
        print(f'Status: {dados_moeda.get('result')}')
        print(f'Chaves do Json: {dados_moeda.keys()}')
        print(f'Data de atualização: {dados_moeda.get('time_last_update_utc')}')
        print(f'Dólar: {dados_moeda.get('rates', {}).get('USD')}')
        print(f'Euro: {dados_moeda.get('rates', {}).get('EUR')}')
    else:
        print('Não foi possível obter os dados da API.')
