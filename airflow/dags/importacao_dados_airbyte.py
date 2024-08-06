from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.airbyte.sensors.airbyte import AirbyteJobSensor
from airflow.sensors.filesystem import FileSensor
import pendulum

AIRBYTE_CONNECTION_ID = '7ac840cb-f369-4423-b41f-07847444ede2'

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
       airbyte_job_id=trigger_airbyte_sync.output
   )

   trigger_airbyte_sync >> wait_for_sync_completion
