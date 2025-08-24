# Importa as configurações e as funções auxiliares
import config
import utils

def main():
    """
    Função principal que orquestra o pipeline de ETL.
    """
    # 1. Extração
    raw_data = utils.extract_data(config.API_URL, config.API_PARAMS)
    
    if raw_data:
        # 2. Transformação
        transformed_df = utils.transform_data(raw_data)
        
        # 3. Carregamento
        utils.load_data(
            df=transformed_df,
            project_id=config.PROJECT_ID,
            destination_table=config.DESTINATION_TABLE
        )

if __name__ == "__main__":
    # Este bloco garante que a função main() só seja executada
    # quando o script é rodado diretamente.
    main()