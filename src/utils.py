import requests
import pandas as pd
from pandas_gbq import to_gbq
import logging

# Configura o logging para exibir mensagens informativas
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_data(url: str, params: dict) -> dict:
    """
    Extrai dados de uma API.

    Args:
        url (str): A URL base da API.
        params (dict): Os parâmetros para a requisição.

    Returns:
        dict: Os dados em formato JSON.
    """
    try:
        logging.info("Iniciando a extração de dados da API...")
        response = requests.get(url, params=params)
        response.raise_for_status()  # Gera um erro para status HTTP ruins (4xx ou 5xx)
        logging.info("Extração de dados concluída com sucesso.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao buscar dados da API: {e}")
        # Em um cenário real, poderíamos ter um sistema de retry aqui.
        # Por enquanto, vamos encerrar a execução se a extração falhar.
        raise

def transform_data(data: dict) -> pd.DataFrame:
    """
    Transforma os dados brutos em um DataFrame do Pandas limpo.

    Args:
        data (dict): Os dados brutos em JSON da API.

    Returns:
        pd.DataFrame: Um DataFrame pronto para ser carregado.
    """
    logging.info("Iniciando a transformação dos dados...")
    df = pd.DataFrame(data['hourly'])
    df['time'] = pd.to_datetime(df['time'])
    df.rename(columns={
        'time': 'data_hora',
        'temperature_2m': 'temperatura_celsius'
    }, inplace=True)
    logging.info("Transformação de dados concluída.")
    return df

def load_data(df: pd.DataFrame, project_id: str, destination_table: str):
    """
    Carrega um DataFrame para uma tabela no Google BigQuery.

    Args:
        df (pd.DataFrame): O DataFrame a ser carregado.
        project_id (str): O ID do projeto no GCP.
        destination_table (str): O nome completo da tabela de destino (dataset.tabela).
    """
    try:
        logging.info(f"Iniciando o carregamento de {len(df)} linhas para a tabela {destination_table}...")
        to_gbq(
            dataframe=df,
            destination_table=destination_table,
            project_id=project_id,
            if_exists='replace'
        )
        logging.info("Dados carregados com sucesso no BigQuery!")
    except Exception as e:
        logging.error(f"Erro ao carregar dados para o BigQuery: {e}")
        raise