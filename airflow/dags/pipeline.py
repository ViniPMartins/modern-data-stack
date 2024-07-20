from airflow.decorators import dag, task
from datetime import datetime

from include.dbt_project.cosmos_config import DBT_PROJECT_PATH, DBT_CONFIG, venv_execution_config
from cosmos import DbtTaskGroup, ProjectConfig, DbtDag
from cosmos.constants import LoadMode
from cosmos.config import ProjectConfig, RenderConfig

from airflow.operators.empty import EmptyOperator
from airflow.models.baseoperator import chain

@dag(
    start_date=datetime(2024, 7, 7),
    schedule=None,
    catchup=False,
    tags=['staging'],
)
def pipeline_movies():
    pre_dbt = EmptyOperator(task_id="pre_dbt")

    transform = DbtTaskGroup(
        group_id='pipeline_staging',
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        profile_config=DBT_CONFIG,
        execution_config=venv_execution_config,
    )

    post_dbt = EmptyOperator(task_id="post_dbt")

    pre_dbt >> transform >> post_dbt

pipeline_movies()