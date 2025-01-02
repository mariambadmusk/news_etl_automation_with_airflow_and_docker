from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from scripts.daily_news_etl import main


# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1, 13, 0),
    'email_on_failure': False,
    'email_on_retry': False,
}


# Define the DAG
with DAG(
    dag_id="daily_news_dag",
    default_args=default_args,
    schedule_interval=timedelta(minutes=10),  
    catchup=False,  
    max_active_runs=1, 
    ) as dag:
    
    # Create a dummy start task
    start_task = DummyOperator(task_id='start_task')

    daily_news_etl = PythonOperator(
        task_id='daily_news_etl_run',  
        python_callable=main,  
        dag=dag
    )
    

     # Create a dummy end task
    end_task = DummyOperator(task_id='end_task')
  

    # Set start_task to trigger the crawl_and_process_category_tasks
    start_task >> daily_news_etl >> end_task  

