Apache Airflow in Python

Links: [Airflow](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html)

```
git status
git add
git commit
```

# airflow needs a home, 
~/airflow is the default, but you can lay foundation somewhere else if you prefer
# (optional)
export AIRFLOW_HOME=~/airflow

# install from pypi using pip
pip install apache-airflow

# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 8080

# start the scheduler
airflow scheduler

# visit localhost:8080 in the browser and enable the example dag in the home pages


# Aiflow CLI commands:
$ airflow dags list

# Errors
$ airflow dags list-import-errors
