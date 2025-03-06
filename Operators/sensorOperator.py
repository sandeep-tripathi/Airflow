from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the default_args dictionary
default_args = {
    'start_date': datetime(2024, 1, 1),
    'depends_on_past': False,
    'retries': 1,
}

# Instantiate the DAG object
with DAG(
    dag_id='file_sensor_example_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:
    # Create the FileSensor task
    file_sensor_task = FileSensor(
        task_id='wait_for_file',
        filepath='/path/to/wait/file.txt',
        fs_conn_id='fs_default',  # Connection ID defined in Airflow connections
        poke_interval=60,  # Check every 60 seconds
        timeout=600,  # Timeout after 10 minutes
        mode='poke',
    )

    # Create the BashOperator task
    process_file_task = BashOperator(
        task_id='process_file',
        bash_command='echo "The file is present!" && cat /path/to/wait/file.txt',
    )

    # Set task dependencies
    file_sensor_task >> process_file_task
