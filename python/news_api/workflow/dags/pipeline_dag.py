import sys
import os
# Dynamically get the current directory
current_file_path = os.path.realpath(__file__)
dags_folder = os.path.dirname(current_file_path)
airflow_folder = os.path.dirname(dags_folder)
project_root = os.path.dirname(airflow_folder)

# Inject the paths dynamically
sys.path.append(project_root)
sys.path.append(os.path.join(project_root, 'venv/lib/python3.12/site-packages'))

from airflow.decorators import dag, task
from datetime import datetime, timedelta
from extract import extract_news
from transform import transform_news
from load import load_news


@dag(
    dag_id="news_pipeline",
    schedule='@daily',
    start_date=datetime(2026, 4, 16),
    catchup=False,
    max_active_runs=1
)
def run_pipeline():
    @task
    def run_extract():
        return extract_news()

    @task
    def run_transform(articles):
        return transform_news(articles)

    @task
    def run_load(transformed_data):
        return load_news(transformed_data)

    raw_data = run_extract()
    clean_data = run_transform(raw_data)
    run_load(clean_data)

run_pipeline()


