import os
import pandas as pd
from datetime import datetime

def salvar_arq(df: pd.DataFrame, update_time_utc: str) -> str:

    data_lake_dir = 'data_lake'
    if not os.path.exists(data_lake_dir):
        os.makedirs(data_lake_dir)

    data_formatada = None
    try:
        data_part = ' '.join(update_time_utc.split()[1:4])
        data_obj = datetime.strptime(data_part, '%d %b %Y')
        data_formatada = data_obj.strftime('%Y-%m-%d')
    except ValueError as erro:
        print(f'Erro ao parsear a data: {erro}. Usando a data atual como fallback.')
        data_formatada = datetime.now().strftime('%Y-%m-%d')

    if data_formatada is None:
        print("Não foi possível formatar a data. Retornando string vazia.")
        return ""

    arquivo_parquet = os.path.join(data_lake_dir, f'cambio_{data_formatada}.parquet')

    try:
        df.to_parquet(arquivo_parquet, index=False, engine='pyarrow')
        print(f'Dados salvos no arquivo: {arquivo_parquet}')
        return arquivo_parquet
    except Exception as e:
        print(f'Erro ao salvar o arquivo Parquet: {e}')
        return ""

if __name__ == "__main__":

    current_time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    amostra = {
        'data': [current_time_str, current_time_str],
        'moeda': ['USD', 'EUR'],
        'cotação': [0.19, 0.17]
    }
    amostra_df = pd.DataFrame(amostra)
    amostra_tempo = 'Sat, 13 Sep 2025 00:02:31 +0000'
    
    salvando_path = salvar_arq(amostra_df, amostra_tempo)

    if salvando_path:
        print(f'Verifique o arquivo em: {salvando_path}')
    else:
        print("Falha ao salvar o arquivo.")

