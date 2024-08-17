from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


with DAG(dag_id='demo', start_date=days_ago(n=0), schedule=timedelta(days=1)) as dag:

    hello = BashOperator(
        task_id='hello',
        bash_command='echo hello'
    )

    @task
    def airflow():
        print("airflow")

    hello >> airflow()
