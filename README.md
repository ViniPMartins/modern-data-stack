# modern-data-stack
Construção de um Modern data stack para processamento  e análise de dados

## Variáveis de ambiente
Definir as seguinte variáveis de ambiente
```
POSTGRES_PASSWORD=password
POSTGRES_USER=postgres
POSTGRES_DB=postgres
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