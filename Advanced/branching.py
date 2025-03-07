from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.dates import days_ago

# Create a function to determine if years are different
def year_check(**kwargs):
    current_year = int(kwargs['ds'][0:4])
    previous_year = int(kwargs['prev_ds'][0:4])
    if current_year == previous_year:
        return 'current_year_task'
    else:
        return 'new_year_task'

# Define the default args
default_args = {
    'start_date': days_ago(1),
}

# Define the DAG
branch_dag = DAG('branch_dag', default_args=default_args, schedule_interval='@daily')

# Define the BranchPythonOperator
branch_task = BranchPythonOperator(
    task_id='branch_task',
    dag=branch_dag,
    python_callable=year_check,
    provide_context=True
)

# Define the tasks
current_year_task = DummyOperator(
    task_id='current_year_task',
    dag=branch_dag
)

new_year_task = DummyOperator(
    task_id='new_year_task',
    dag=branch_dag
)

# Set the dependencies
branch_task >> current_year_task
branch_task >> new_year_task
