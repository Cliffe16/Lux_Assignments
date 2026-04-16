from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
from extract import extract_news
from transform import transform_news
from load import load_news


with DAG(
    dag_id="news_pipeline",
    schedule='@daily',
    start_date=datetime(2026, 4, 16),
    catchup=False,
    max_active_runs=1
) as dag:
    task_extract = PythonOperator(
        task_id='extract_news',
        python_callable=extract_news
        )
    task_transform = PythonOperator(
        task_id='transform_news',
        python_callable=transform_news
        )
    task_load = PythonOperator(
        task_id='load_news',
        python_callable=load_news
        )

task_extract >> task_transform >> task_load
