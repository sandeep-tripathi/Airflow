from datetime import datetime, timedelta
from airflow import DAG

# Update the scheduling arguments as defined
default_args = {
  'owner': 'Engineering',
  'start_date': datetime(2023, 11, 1),
  'email': ['airflowresults@datacamp.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 3,
  'retry_delay': timedelta(minutes=20)
}
# run every Wednesday at 12:30 PM using the cron syntax '30 12 * * 3'
dag = DAG('update_dataflows', default_args=default_args, schedule_interval='30 12 * * 3')
