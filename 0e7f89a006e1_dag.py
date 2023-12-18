from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator
from datetime import datetime, timedelta

# Define parameters for the Submit Run Operator
notebook_task = {
    'notebook_path': '/Users/asif1232@hotmail.co.uk/Batch Processing S3 Data',
}

# Define parameters for the Run Now Operator
notebook_params = {
    "Variable": 5
}

# Define default arguments for the DAG
default_args = {
    'owner': 'sai charan',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

# Define the DAG
with DAG('12c8b0153527_dag',
         start_date=datetime(2023, 8, 20),  # Start date for the DAG execution
         schedule_interval='@daily',  # DAG schedule interval
         catchup=False,  # Whether to catch up on missed DAG runs
         default_args=default_args  # Default arguments for the DAG
         ) as dag:

    # Databricks Submit Run Operator
    opr_submit_run = DatabricksSubmitRunOperator(
        task_id='submit_run',
        databricks_conn_id='databricks_default',  # Databricks connection ID
        existing_cluster_id='1108-162752-8okw8dgg',  # ID of the existing Databricks cluster
        notebook_task=notebook_task  # Parameters for the notebook task
    )
    opr_submit_run  # Adding the operator to the DAG
