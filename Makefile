all: airbyte airflow connect-networks superset

wout-ss: airbyte airflow connect-networks

airbyte:
	if [ ! -d "airbyte" ]; then git clone --depth=1 https://github.com/airbytehq/airbyte.git; fi
	./airbyte/run-ab-platform.sh -b

airflow: init-astro connect-networks

init-astro: install-astro-cli
	cd airflow && astro dev start --no-cache -n

stop-astro:
	cd airflow && astro dev stop

connect-networks: airbyte airflow
	docker network connect airflow_cad268_airflow airbyte-proxy

install-astro-cli:
	curl -sSL install.astronomer.io | sudo bash -s

superset:
	if [ ! -d "superset" ]; then git clone --depth=1 https://github.com/apache/superset.git; fi
	cd superset && docker compose -f docker-compose-non-dev.yml up -d
	docker network connect airflow_cad268_airflow superset_app
