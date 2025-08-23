# =============================================================================
# BIBLIOTECAS
# =============================================================================
import requests
import pandas as pd
from pandas_gbq import to_gbq # Importa a função específica para carregar dados no BigQuery

# =============================================================================
# PASSO 1: EXTRAÇÃO
# =============================================================================
print("Iniciando a extração de dados da API...")

# Define a URL da API Open-Meteo
url = "https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.64&hourly=temperature_2m"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("Extração de dados concluída com sucesso.")
except requests.exceptions.RequestException as e:
    print(f"Erro ao buscar dados da API: {e}")
    exit() # Encerra o script se a extração falhar

# =============================================================================
# PASSO 2: TRANSFORMAÇÃO
# =============================================================================
print("Iniciando a transformação dos dados...")

# A parte mais importante dos dados está na chave 'hourly'.
# O Pandas consegue transformar um dicionário de listas em uma tabela (DataFrame) diretamente!
df = pd.DataFrame(data['hourly'])

# A coluna 'time' vem como texto. Vamos convertê-la para um formato de data/hora real.
# Isso é crucial para análises de tempo no BigQuery.
df['time'] = pd.to_datetime(df['time'])

# Vamos renomear as colunas para português e para um padrão mais limpo.
df.rename(columns={
    'time': 'data_hora',
    'temperature_2m': 'temperatura_celsius'
}, inplace=True)

print("Transformação de dados concluída.")

# --- PONTO DE VERIFICAÇÃO ---
# Vamos verificar a estrutura e as primeiras linhas da nossa tabela transformada.
print("\nInformações do DataFrame transformado:")
print(df.info())

print("\n5 primeiras linhas dos dados:")
print(df.head())


# =============================================================================
# PASSO 3: CARREGAMENTO (LOAD)
# =============================================================================
print("\nIniciando o carregamento dos dados para o BigQuery...")

# --- ATENÇÃO: CONFIGURE SUAS VARIÁVEIS AQUI ---
# Substitua pelo ID do seu projeto no GCP.
project_id = 'graceful-tenure-469816-p4' 
# O nome da tabela que será criada no BigQuery.
# O formato é 'seu_dataset.nome_da_tabela'
destination_table = 'meu_primeiro_pipeline.previsao_tempo_sp' 

try:
    # A função to_gbq faz todo o trabalho pesado:
    # 1. Conecta ao BigQuery usando a autenticação que configuramos (gcloud).
    # 2. Cria a tabela se ela não existir.
    # 3. Carrega os dados do DataFrame para a tabela.
    to_gbq(
        dataframe=df,
        destination_table=destination_table,
        project_id=project_id,
        if_exists='replace' # 'replace' apaga a tabela antiga e cria uma nova. Perfeito para nosso caso!
                           # Outras opções: 'fail' (falha se a tabela existir), 'append' (adiciona os dados no final).
    )
    print("Dados carregados com sucesso no BigQuery!")
    print(f"Tabela '{destination_table}' atualizada no projeto '{project_id}'.")

except Exception as e:
    print(f"Erro ao carregar dados para o BigQuery: {e}")