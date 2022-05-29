import pendulum
from datetime import datetime

from airflow import DAG, settings, secrets
from airflow.operators.dummy import DummyOperator
from airflow.operators.subdag import SubDagOperator
from airflow.utils.dates import days_ago
from airflow.utils.helpers import chain


local_tz = pendulum.timezone("America/Sao_Paulo")
yday = datetime(2021,1,1).astimezone(local_tz)

default_args = {
    'start_date': yday,
}

with DAG(
        dag_id='TEST_ENVIRONMENT',
        default_args=default_args, 
        schedule_interval='0 6 * * 2-6', 
        catchup=False
) as dag:

    extract = DummyOperator(task_id='reach_api')

    clean_tasks = DummyOperator(task_id='clean')
    
    process_tasks = DummyOperator(task_id='process')

    store = DummyOperator(task_id='store')

    chain(extract, clean_tasks, process_tasks, store)