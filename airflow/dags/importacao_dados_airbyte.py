from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.bash import BashOperator
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.airbyte.sensors.airbyte import AirbyteJobSensor
from airflow.sensors.filesystem import FileSensor
import pendulum

AIRBYTE_CONNECTION_ID = '313a73ec-046d-4c33-b22c-b6e59b8f9d22'

dataset_name = "airbyte_sync_dataset"
airbyte_sync_dataset = Dataset(dataset_name)

with DAG(dag_id='airbyte_airflow_dag',
        default_args={'owner': 'airflow'},
        schedule=None,
        start_date=pendulum.today('UTC').add(days=-1)
   ) as dag:

   trigger_airbyte_sync = AirbyteTriggerSyncOperator(
       task_id='airbyte_trigger_sync',
       airbyte_conn_id='airbyte',
       connection_id=AIRBYTE_CONNECTION_ID,
       asynchronous=True
   )

   wait_for_sync_completion = AirbyteJobSensor(
       task_id='airbyte_check_sync',
       airbyte_conn_id='airbyte',
       airbyte_job_id=trigger_airbyte_sync.output,
       outlets=[airbyte_sync_dataset]
   )

   trigger_airbyte_sync >> wait_for_sync_completion
