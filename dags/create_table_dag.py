from datetime import timedelta
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta
from scripts.utils import get_database_connection, setup_logging


logger = setup_logging()

def create_tables():
    try:
        connection = get_database_connection()
        connection.autocommit = True
        cursor = connection.cursor()

        # Path to the SQL file within the scripts directory
        sql_file_path = "dags/scripts/create_table.sql"

        with open(sql_file_path, 'r') as sql_file:
            sql_commands = sql_file.read()
            
        cursor.execute(sql_commands)
        logger.info("Tables created successfully")
        
    except Exception as e:
        logger.error(f"Error creating tables: {e}")
        raise
    finally:
        cursor.close()
        connection.close()

default_args = {
    "owner": "aiflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}

with DAG(
    dag_id="create_table_dag",
    default_args=default_args,
    description="One-time DAG to create initial database tables",
    schedule_interval=None,  
    start_date=datetime(2024, 1, 1),
    catchup=False,  
    tags=['setup', 'one-time']
) as dag:
    
    # Create a dummy start task
    start_task = DummyOperator(task_id='start_task')


    create_tables_task = PythonOperator(
        task_id='create_tables',
        python_callable=create_tables,
        doc_md="""Creates required database tables if they don't exist."""
    )

    
     # Create a dummy end task
    end_task = DummyOperator(task_id='end_task')

    start_task >> create_tables_task >> end_task  