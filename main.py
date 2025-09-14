from api import cambios
from transformacao import transfomar_data
from data_lake import salvar_arq
from organizacao import dados_curated
from visu import grafico_cotacoes_direto

def main():
    print('Iniciando o processo de Elt de cotação.....')

    # EXTRAÇÃO.
    print('\n1. Extraindo dados da API.....')
    api_data = cambios()
    if not api_data:
        print('Falha na Extração. Encerrando processo')
        return
    print("Dados da Extraidos com sucesso.")

    # Transformação
    print('\n2. Transformando os dados...')
    df = transfomar_data(api_data)
    if df.empty:
        print('Falha na transformação. Encerrando processo')
        return
    print('Dados transformado com sucesso.')

    #Carregando na Data Lake
    print('\n3. Carregando dados no Data lake....')
    parquet_file = salvar_arq(df, api_data["time_last_update_utc"])
    if not parquet_file:
        print('Falha ao salvar dados no Data lake. Encerrando processo')
        return
    print(f'Dados salvo em: {parquet_file}')

    # Organizando e curando
    print('\n4. Processando dados e curando...' )
    dados_curated(parquet_file)
    print("Processo de curadoria concluido.")
    print("\nPrograma de contação concluído!!")

   # GERAÇÃO  DE GRAFICO
    print("\n5. Gerando visualizações...")
    caminho_grafico = grafico_cotacoes_direto('graficos_output')
    if caminho_grafico:
        print(f"Visualização gerada e salva em: {caminho_grafico}")
    else:
        print("Falha ao gerar visualização.")

    print("\nPrograma de cotação concluído!!\n")


if __name__ == "__main__":
    main()