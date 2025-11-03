from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'email': ['xyz123@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='order_monitor_dag',
    default_args=default_args,
    schedule_interval='@hourly',
    start_date=days_ago(1),
    catchup=False
) as dag:

    dbt_run = BashOperator(
        task_id='run_dbt_models',
        bash_command='source "C:/Users/nyasa/Desktop/E-Commerce/airflow_env/Scripts/activate" && cd "C:/Users/nyasa/Desktop/E-Commerce/dbt_ecommerce" && dbt run'
    )

    check_orders = BashOperator(
        task_id='check_delayed_orders',
        bash_command='source "C:/Users/nyasa/Desktop/E-Commerce/airflow_env/Scripts/activate" && python "C:/Users/nyasa/Desktop/E-Commerce/airflow_part/dags/utils/check_delayed_orders.py"'
    )

    dbt_run >> check_orders 
