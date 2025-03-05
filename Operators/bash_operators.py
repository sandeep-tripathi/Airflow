from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the default_args dictionary
default_args = {
    'start_date': datetime(2024, 1, 1)
}

# Instantiate the DAG object
with DAG(dag_id="test_dag", default_args=default_args, schedule_interval='@daily') as analytics_dag:
    # Define the first BashOperator to run cleanup.sh
    cleanup = BashOperator(
        task_id='cleanup_task',
        bash_command='cleanup.sh',
    )

    # Define a second operator to run the consolidate_data.sh script
    consolidate = BashOperator(
        task_id='consolidate_task',
        bash_command='consolidate_data.sh'
    )

    # Define a final operator to execute the push_data.sh script
    push_data = BashOperator(
        task_id='pushdata_task',
        bash_command='push_data.sh'
    )

# Upstream: shift operator '>>' means before 
# Downstream: '<<' means after

    # Set the task dependencies
    cleanup >> consolidate >> push_data
