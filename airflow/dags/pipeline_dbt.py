from airflow.decorators import dag, task
from datetime import datetime

from include.dbt_project.cosmos_config import DBT_PROJECT_PATH, DBT_CONFIG, venv_execution_config
from cosmos import DbtTaskGroup, ProjectConfig, DbtDag
from cosmos.constants import LoadMode
from cosmos.config import ProjectConfig, RenderConfig

from airflow.operators.empty import EmptyOperator
from airflow.models.baseoperator import chain
from airflow.datasets import Dataset

airbyte_sync_dataset = Dataset("airbyte_sync_dataset")

@dag(
    start_date=datetime(2024, 7, 7),
    schedule=[airbyte_sync_dataset],
    catchup=False,
    tags=['airflow'],
)
def pipeline_dbt():
    pre_dbt = EmptyOperator(task_id="pre_dbt")

    transform_prata = DbtTaskGroup(
        group_id='camada_prata',
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        profile_config=DBT_CONFIG,
        execution_config=venv_execution_config,
        render_config=RenderConfig(
            select=['path:models/prata']
        )
    )

    transform_ouro = DbtTaskGroup(
        group_id='camada_ouro',
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        profile_config=DBT_CONFIG,
        execution_config=venv_execution_config,
        render_config=RenderConfig(
            select=['path:models/ouro']
        )
    )

    post_dbt = EmptyOperator(task_id="post_dbt")

    pre_dbt >> transform_prata >> transform_ouro >> post_dbt

pipeline_dbt()