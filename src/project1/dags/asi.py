from datetime import timedelta

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

from project1.script.download_file import get_file

# SFTP server credentials
hostname = "172.25.249.11"
port = 22  # default SFTP port
username = "cp"
password = "1"  # or use a private key file

with DAG(
    dag_id="asi",
    start_date=days_ago(n=0),
    schedule=timedelta(days=1),
    tags=["asi"],
) as dag:
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task
    def airflow():
        print("airflow")

    hello >> airflow() >> get_file()
