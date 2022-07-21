import airflow
from airflow import DAG
from datetime import datetime

#Create and instance of a DAG class
dag = DAG(
    dag_id="nyc_dag",
    schedule_interval="@daily", 
    start_date=airflow.utils.dates.days_ago(1),
    catchup=False,
)

#implementing the tasks
