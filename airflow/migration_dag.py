from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def migrate():
    print("Executing SAS migration")

with DAG(
    dag_id='sas_migration_pipeline',
    start_date=datetime(2024,1,1),
    catchup=False
) as dag:

    migrate_task = PythonOperator(
        task_id='migrate_jobs',
        python_callable=migrate
    )
