import pandas as pd
from datetime import datetime

def transfomar_data(data):
    if not data or 'rates' not in data or 'time_last_update_utc' not in data:
        print("Dados da API inválidos ou incompletos para transformação.")
        return pd.DataFrame()
    
    moedas = list(data['rates'].keys())
    linha = []
    data_formatada = None

    try:
        data_str = data['time_last_update_utc']
        data_part = ' '.join(data_str.split()[1:4])
        data_obj = datetime.strptime(data_part, "%d %b %Y")
        data_formatada = data_obj.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        print(f'Erro ao parsear a data')
        data_formatada = data['time_last_update_utc'] 


    if data_formatada is None:
        print("Não foi possível formatar a data. Retornando DataFrame vazio.")
        return pd.DataFrame()

    for moeda_item in moedas: 

        linha.append({
            'data': data_formatada,
            'moeda': moeda_item,
            'cotação': data['rates'][moeda_item]
        })

    df = pd.DataFrame(linha)
    return df

if __name__ == "__main__":
    amostra = {
        'result': 'success',
        'documentation': 'https://open.er-api.com/v6/documentation',
        'terms_of_use': 'https://open.er-api.com/v6/terms',
        'time_last_update_unix': 1678838400,
        'time_last_update_utc': 'Sat, 13 Sep 2025 00:02:31 +0000',
        'time_next_update_unix': 1678924800,
        'time_next_update_utc': 'Sun, 14 Sep 2025 00:02:31 +0000',
        'base_code': 'BRL',
        'rates': {
            'BRL': 1.0,
            'USD': 0.19,
            'EUR': 0.17,
            'GBP': 0.15,
            'JPY': 147.00,
            'CAD': 1.35,
            'AUD': 1.55
        }
    }
    df_transformado = transfomar_data(amostra)
    if not df_transformado.empty:
        print(df_transformado.head())
        print(f"\nTotal de moedas: {len(df_transformado)}")
    else:
        print("DataFrame transformado está vazio ou houve um erro.")