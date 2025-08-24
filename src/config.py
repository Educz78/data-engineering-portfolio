# Configurações da API
API_URL = "https://api.open-meteo.com/v1/forecast"
API_PARAMS = {
    "latitude": -23.55,
    "longitude": -46.64,
    "hourly": "temperature_2m",
    "timezone": "America/Sao_Paulo"
}

# Configurações do BigQuery
PROJECT_ID = 'graceful-tenure-469816-p4' 
DESTINATION_TABLE = 'meu_primeiro_pipeline.previsao_tempo_sp'