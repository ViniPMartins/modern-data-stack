# modern-data-stack
Construção de um Modern data stack para processamento  e análise de dados

## Variáveis de ambiente
Definir as seguinte variáveis de ambiente
```
POSTGRES_HOST=host
POSTGRES_PORT=port
POSTGRES_PASSWORD=password
POSTGRES_USER=user
POSTGRES_DB=database
DBT_PROFILES_DIR=/path/to/profile
```

## Primeiros passos
Na raiz principal do projeto, subir o container com o postgres com o comando

```bash
docker compose up
```
Em seguida, subir o Airbyte com os seguintes comandos

```bash
# switch into Airbyte directory
cd airbyte

# start Airbyte
./run-ab-platform.sh
```

Caso ainda não tenha a pasta do Airbyte, é necessário clonar o repositório
```bash
# clonar o Airbyte do github caso ainda n
git clone --depth=1 https://github.com/airbytehq/airbyte.git
```

Iniciar o Airflow com o seguinte comando
```bash
astro dev start
```

Se precisar instalar o Astro Cli, ver [essa documentação](https://www.astronomer.io/docs/astro/cli/install-cli)

Caso tenha conflito de postas, olhar [essa documentação](https://www.astronomer.io/docs/astro/cli/troubleshoot-locally#ports-are-not-available-for-my-local-airflow-webserver)


Para configurar o DBT, verique se está instalado. Se não, usar:
```bash
pip install dbt-postgres
```

Para iniciar um projeto e testar, rodar os seuintes comandos:
```bash
dbt init
dbt debug
```
Para definir a pasta onde será salvo e lido pelo dbt o arquivo profiles.yml, a variável de ambiente `DBT_PROFILES_DIR` deve estar iniciada no ambiente.
