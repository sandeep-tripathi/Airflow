import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime
import json

# Define the pull_file function
def pull_file(URL, savepath):
    r = requests.get(URL)
    with open(savepath, 'wb') as f:
        f.write(r.content)
    print(f"File pulled from {URL} and saved to {savepath}")

# Assuming parse_file is already defined for you as follows
def parse_file(inputfile, outputfile):
    with open(inputfile, 'r') as f:
        data = json.load(f)
    # Placeholder for parsing logic; modify `data` as needed
    parsed_data = data
    with open(outputfile, 'w') as f:
        json.dump(parsed_data, f)
    print(f"File parsed from {inputfile} and saved to {outputfile}")

# Define the default_args dictionary
default_args = {
    'start_date': datetime(2024, 1, 1)
}

# Instantiate the DAG object
with DAG(dag_id="file_pull_dag", default_args=default_args, schedule_interval='@daily') as dag:
    # Create the pull_file_task
    pull_file_task = PythonOperator(
        task_id='pull_file',
        python_callable=pull_file,
        op_kwargs={'URL': 'http://dataserver/sales.json', 'savepath': 'latestsales.json'}
    )

    # Create the parse_file_task
    parse_file_task = PythonOperator(
        task_id='parse_file',
        python_callable=parse_file,
        op_kwargs={'inputfile': 'latestsales.json', 'outputfile': 'parsedfile.json'}
    )

    # Create the email_manager_task
    email_manager_task = EmailOperator(
        task_id='email_manager',
        to='manager@datacamp.com',
        subject='Latest sales JSON',
        html_content='Attached is the latest sales JSON file as requested.',
        files=['parsedfile.json'],  # Ensure this is a list of file paths
        dag=dag
    )

    # Set the order of tasks
    pull_file_task >> parse_file_task >> email_manager_task
