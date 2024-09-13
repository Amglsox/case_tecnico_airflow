SHELL=/bin/bash

.DEFAULT_GOAL := help

.PHONY: help
help: ## Shows this help text
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	

.PHONY: start-airflow
start-airflow: ## Start Airflow
	mkdir -p ./dags ./logs ./plugins ./data
	echo -e "AIRFLOW_UID=$$(id -u)" > .env
	docker-compose -f ./docker-compose.yaml up -d

.PHONY: down-airflow
down-airflow: ## Down Airflow
	docker-compose -f ./docker-compose.yaml down --remove-orphans
