# 📊 Projeto de Pipeline de Cotações Cambiais  

Este projeto implementa um **pipeline de dados** para consultar, transformar, armazenar e visualizar informações de cotações de moedas.  
A ideia central é simular um processo de **ELT (Extract, Load, Transform)** em um fluxo simples, mas com boas práticas de organização.

---

## 🔑 Principais Etapas do Projeto  

### 1. **Extração de Dados (API)**
- O módulo [`api.py`](./api.py) consulta a API [Open Exchange Rates](https://open.er-api.com/v6/latest/BRL) (ou similar) para obter as taxas de câmbio.  
- Caso a API esteja indisponível, há tratamento de erros para evitar falhas no processo.  

### 2. **Transformação**
- O módulo [`transformacao.py`](./transformacao.py) organiza os dados extraídos.  
- As informações são convertidas em um **DataFrame do pandas**, contendo:
  - Data da atualização  
  - Moeda  
  - Cotação em relação ao **BRL**  
- A data vinda da API é padronizada para facilitar análises posteriores.

### 3. **Armazenamento no Data Lake**
- Em [`data_lake.py`](./data_lake.py), os dados transformados são salvos em **formato Parquet**, dentro da pasta `data_lake/`.  
- O nome do arquivo inclui a data da atualização, facilitando versionamento e histórico.  
- Esse formato foi escolhido por ser compacto e eficiente para consultas.

### 4. **Curadoria e Organização**
- O módulo [`organizacao.py`](./organizacao.py) processa os dados salvos e gera arquivos derivados, como:
  - `media.csv` → contendo a média das cotações.  
- Essa camada representa a área **curated** do Data Lake (`data_lake/curated`).

### 5. **Visualização**
- O módulo [`visu.py`](./visu.py) gera **gráficos simulados** de evolução das moedas ao longo de 10 anos.  
- As visualizações são salvas automaticamente em `graficos_output/`.  
- Foram utilizadas as bibliotecas **Matplotlib** e **Seaborn** para criar gráficos claros e bem formatados.

### 6. **Orquestração**
- O arquivo principal [`main.py`](./main.py) integra todas as etapas:
  1. Extrai os dados da API  
  2. Transforma em DataFrame  
  3. Salva no Data Lake  
  4. Executa a curadoria  
  5. Gera as visualizações  

---

## 🚀 Como Executar  

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/projeto-cambio.git
   cd projeto-cambio
   ```

2. Instale as dependências:  
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o pipeline:  
   ```bash
   python main.py
   ```

---

## 📂 Estrutura de Pastas  

```
projeto-cambio/
│── api.py              # Extração de dados da API
│── transformacao.py    # Transformação dos dados em DataFrame
│── data_lake.py        # Salvamento em Parquet
│── organizacao.py      # Curadoria dos dados
│── visu.py             # Visualização (gráficos)
│── main.py             # Orquestração do pipeline
│── data_lake/          # Armazenamento dos dados brutos
│   └── curated/        # Dados curados (ex: médias)
│── graficos_output/    # Saída dos gráficos
│── requirements.txt    # Dependências do projeto
```

---

## 📌 Observações
- O pipeline foi estruturado de forma **modular**, permitindo evolução futura (como conexão com banco de dados, dashboards no Power BI, ou agendamento automático).  
- O objetivo é **simular o fluxo real de um engenheiro/analista de dados**, mas em um escopo didático.  
