import pandas as pd
import os

def dados_curated(parquet_file_path: str) -> None:

    curated_dir = 'data_lake/curated'
    os.makedirs(curated_dir, exist_ok=True)

    try:
        df = pd.read_parquet(parquet_file_path, engine='pyarrow')

        if 'cotação' in df.columns:
            df_mean = df['cotação'].mean()
            file_csv = os.path.join(curated_dir, 'media.csv')
            pd.Series({'media_cotacao': df_mean}).to_csv(file_csv, header=False)
            print(f'Media de Cotação salva em: {file_csv}')
        else:
            print('Coluna "cotação" não encontrada no DataFrame.')


    except FileNotFoundError:
        print(f'Erro: Arquivo não encontrado {parquet_file_path}')
    except Exception as e:
        print(f'Erro ao processar dados curados: {e}')

if __name__ == "__main__":
    test_parquet_path = "data_lake/cambio_2025-09-13.parquet" 

    if os.path.exists(test_parquet_path):
        dados_curated(test_parquet_path)
    else:
        print(f"Arquivo de teste {test_parquet_path} não encontrado. Por favor, gere-o primeiro.")

