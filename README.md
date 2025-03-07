Apache Airflow in Python

Links: [Airflow](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html)

# Common commands
```
pip install apache-airflow   # Installation
export AIRFLOW_HOME=~/airflow
airflow initdb
airflow webserver -p 8080    # visit localhost:8080 in the browser

airflow tasks test <dag_id> <task_id> <date> # Run specific task from command
airflow dags trigger -e <date>  <dag_id>  # Run full dag
airflow scheduler
airflow dags list
airflow dags list-import-errors
airflow info
```





