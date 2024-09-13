# Desafio: Pipeline de Extração, Transformação e Armazenamento com Dados de Câmbio
**Objetivo:** Criar um DAG no Airflow que:

Baixe dados de taxas de câmbio de uma API pública Fixer.io.

1.   Transforme os dados, filtrando as taxas de câmbio para uma moeda específica (ex: USD para EUR, GBP, BRL).
2.   Armazene os dados transformados em um arquivo CSV local.

# Instruções:

**1.   Criação do DAG:**
Crie um DAG com 3 tarefas:

*   **Task 1:** Baixar dados de uma API pública de taxas de câmbio Fixer.io.
*   **Task 2:**  Implemente uma função que transforme e filtre os dados de câmbio obtidos pela Task 1. A função deve retornar um dicionário contendo apenas as taxas de euro, libra, real brasileiro, dólar, além da data de execução da DAG.
*   **Task 3:** Armazenar os dados filtrados em um arquivo CSV local.

**2. Detalhes Técnicos:**

* O DAG deve ser agendado para rodar diariamente.
* A DAG faz o download das taxas de câmbio da API Fixer.io, abrangendo o período de 1º de setembro de 2024 até o dia anterior à data atual.
* O caminho para armazenar o arquivo CSV deve ser configurável via variável do Airflow. Cada dia de execução deve ser organizado em uma subpasta separada, seguindo o formato de data. 
* As dependências entre as tarefas devem ser claramente definidas (ex: a Task 2 só deve começar após a Task 1 terminar, e assim por diante).

# Documentação de apoio: 
1. https://airflow.apache.org/docs/apache-airflow/stable/index.html
2. https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html
3. https://requests.readthedocs.io/en/latest/
4. https://docs.python.org/3/library/csv.html
