from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.decorators import task
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

# Definição do DAG
default_args = {
    'owner': 'airflow',
    'start_date': None
}
"""
Crie uma DAG que faça o download das taxas de câmbio de uma URL específica, abrangendo o período de 1º de setembro de 2024 até o dia anterior à data atual.
"""
@dag(default_args=default_args, 
     schedule_interval=None)
def teste_tecnico_exchange_rate_pipeline() -> None:
    start_dag = EmptyOperator(task_id="start_dag")
    end_dag = EmptyOperator(task_id="end_dag")

    @task()
    def download_data(ds=None):
        """
        Crie aqui uma função que faça o download dos dados de câmbio de uma URL específica.
        Exemplo de Retorno da API:
        {
        "success": true,
        "timestamp": 1726152858,
        "base": "EUR",
        "date": "2024-09-12",
        "rates": {
            "CAD": 1.501908,
            "CDF": 3169.327221,
            "CHF": 0.94303,
            "CLF": 0.037543,
            "CLP": 1036.215039,
            "CNY": 7.858605,
            "EUR": 1,
            "FJD": 2.452417,
            "FKP": 0.859717,
            "GBP": 0.844278,
            "GEL": 2.97604,
            "GGP": 0.859717,
            "GHS": 17.344976,
            "XCD": 2.984413,
            "XDR": 0.818847,
            "XOF": 657.514104,
            "XPF": 119.331742,
            "YER": 276.460421,
            "ZAR": 19.732606,
            "ZMK": 9939.982554,
            "ZMW": 29.026901,
            "ZWL": 355.58259
        }
        }
        Parameters:
        - ds (str) 

        Returns:
        - dict: Os dados baixados.
        """
        data = '2024-09-12'
        url = f"https://data.fixer.io/api/{data}?access_key=f2de9c088d4a1e713bfa5cd7105cc50b"
        print(url)
        pass
        
    
    @task()
    def transform_exchange_rates(ti, ds=None):
        """
        
        Implemente uma função que transforme e filtre os dados de câmbio obtidos pela função download_data. 
        A função deve retornar um dicionário contendo apenas as taxas de EUR, GBP, BRL, USD, além da data de execução da DAG.

        Parameters:
        - ti (TaskInstance) 
        - ds (str, optional)

        Returns:
        - dict: Um dicionário contendo as taxas de câmbio relevantes para EUR, GBP, BRL, USD e a data de execução.
        """
        pass
    
    @task()
    def save_rates_to_csv(ti, ds=None):
        """
       Implemente uma função que salve os dados coletados da API em um arquivo CSV, armazenando os arquivos na pasta /opt/airflow/data. 
       Cada dia de execução deve ser organizado em uma subpasta separada, seguindo o formato de data. 
       Exemplos de caminhos gerados para os arquivos:
        - /opt/airflow/data/2024-09-01/exchange_rates.csv
        - /opt/airflow/data/2024-09-02/exchange_rates.csv
        - /opt/airflow/data/2024-09-03/exchange_rates.csv

        Parameters:
            - ti (TaskInstance)
            - ds (str, optional)
        Returns:
        None
        """
        import os
        filename = f'/opt/airflow/data/1900-01-01/exchange_rates.csv'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        pass

    start_dag >> download_data() >> transform_exchange_rates() >> save_rates_to_csv() >> end_dag

teste_tecnico_exchange_rate_pipeline()