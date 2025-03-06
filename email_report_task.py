from airflow.operators.email import EmailOperator

# Assuming you've already defined your DAG named report_dag and the generate_report task
report_dag = DAG('report_workflow', start_date=datetime(2024, 1, 20), schedule_interval='@monthly')

generate_report = BashOperator(
    task_id='generate_report',
    bash_command='generate_report.sh',
    dag=report_dag
)

# Define the email task
email_report = EmailOperator(
    task_id='email_report',
    to='airflow@datacamp.com',
    subject='Airflow Monthly Report',
    html_content="""Attached is your monthly workflow report - please refer to it for more detail""",
    files=['/path/to/monthly_report.pdf'],
    dag=report_dag
)

# Set the email task to run after the report is generated
generate_report >> email_report
