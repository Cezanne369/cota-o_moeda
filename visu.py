import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import numpy as np 

def gerar_dados_simulados(num_days=365 * 10):

    data_list = []
    
    initial_rates = {
        'BRL': 1.0,
        'USD': 0.19,
        'EUR': 0.17,
        'GBP': 0.15,
        'JPY': 147.00,
        'CAD': 1.35,
        'AUD': 1.55
    }

    start_date = datetime.now() - timedelta(days=num_days - 1)

    np.random.seed(42) 
    daily_fluctuations = {
        moeda: np.random.randn(num_days) * (0.001 if moeda not in ['JPY'] else 0.5) 
        for moeda in initial_rates.keys() if moeda != 'BRL'
    }

    for i in range(num_days):
        current_date = start_date + timedelta(days=i)
        
        for moeda, initial_cotacao in initial_rates.items():
            cotacao = initial_cotacao
            if moeda == 'BRL': 
                cotacao = 1.0
            else:
                cotacao += np.sum(daily_fluctuations[moeda][:i+1])
                cotacao = max(0.01, cotacao)

            data_list.append({
                "data": current_date,
                "moeda": moeda,
                "cotação": cotacao
            })
            
    df_simulado = pd.DataFrame(data_list)
    return df_simulado

def grafico_cotacoes_direto(output_dir):

    os.makedirs(output_dir, exist_ok=True)

    df_consolidado = gerar_dados_simulados(num_days=365 * 10) 

    df_consolidado = df_consolidado.sort_values(by="data")

    moedas_desejadas = ["BRL", "USD", "EUR", "GBP", "JPY", "CAD", "AUD"]
    df_filtrado = df_consolidado[df_consolidado["moeda"].isin(moedas_desejadas)]

    if df_filtrado.empty:
        print("Nenhum dado para as moedas desejadas foi encontrado após a filtragem.")
        return ""

    sns.set_theme(style="whitegrid", palette="viridis") 
    plt.figure(figsize=(18, 9)) 
    
    sns.lineplot(data=df_filtrado, x="data", y="cotação", hue="moeda", linewidth=2.5, alpha=0.8)

    plt.title("Evolução das Cotações das Principais Moedas (10 Anos Simulados)", fontsize=18, fontweight="bold") 
    plt.xlabel("Data", fontsize=14) 
    plt.ylabel("Cotação", fontsize=14) 
    
    plt.legend(title="Moeda", bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0., fontsize=10, title_fontsize=12) 
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gcf().autofmt_xdate()

    plt.grid(True, linestyle="-", alpha=0.5) # GRADE MAIS VISÍVEL
    
   
    plt.ylim(0, 2) 

    plt.tight_layout(rect=[0, 0, 0.88, 1])  # pyright: ignore[reportArgumentType]

    chart_filename = f"cotacoes_historicas_simuladas_estilo_2_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png"
    chart_path = os.path.join(output_dir, chart_filename)
    plt.savefig(chart_path, dpi=300)
    print(f"Gráfico salvo em: {chart_path}")
    plt.close()

    return chart_path

if __name__ == "__main__":
    output_directory = "graficos_cotacoes_diretos"
    caminho_grafico = grafico_cotacoes_direto(output_directory)
    if caminho_grafico:
        print(f"Gráfico gerado com sucesso em: {caminho_grafico}")
    else:
        print("Falha ao gerar o gráfico.")
