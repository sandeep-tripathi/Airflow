from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

# Define default args
default_args = {
    'email': ['airflow@datacamp.com'],
    'email_on_failure': True,
    'email_on_success': True,
}

# Define DAG
report_dag = DAG(
    dag_id='execute_report',
    schedule_interval="0 0 * * *",
    default_args=default_args,
    start_date=datetime(2023, 2, 20),
    catchup=False  # Avoid backfilling for dates before the start_date
)

# Define tasks
precheck = FileSensor(
    task_id='check_for_datafile',
    filepath='salesdata_ready.csv',
    start_date=datetime(2023, 2, 20),
    mode='reschedule',
    dag=report_dag
)

generate_report_task = BashOperator(
    task_id='generate_report',
    bash_command='generate_report.sh',
    start_date=datetime(2023, 2, 20),
    dag=report_dag
)

# Set task dependencies
precheck >> generate_report_task

