from cosmos.config import ProfileConfig, ProjectConfig
from pathlib import Path
from cosmos.profiles import PostgresUserPasswordProfileMapping
from cosmos import ExecutionConfig
from pathlib import Path

DBT_CONFIG = ProfileConfig(
    profile_name="airflow_db",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="airflow_db",
        profile_args={"schema": "bi"},
    ),
)

DBT_PROJECT_PATH = Path('/usr/local/airflow/include/dbt_project/')
dbt_executable = Path("/usr/local/airflow/dbt_venv/bin/dbt")

venv_execution_config = ExecutionConfig(
    dbt_executable_path=str(dbt_executable),
)