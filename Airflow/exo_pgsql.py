from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import psycopg2
import pandas as pd

default_args = {
    'owner': 'Groupe Data',
    'start_date': datetime(2021, 10, 26)
}

XYZ = DAG('data_exo_pgsql', default_args=default_args)

####### Definition des Fonctions / Executions #######

def python_fct1(**kwargs):
    # Reading TI, Task Instance from KWargs
    connection = psycopg2.connect(user="postgres",
                                  password="123456789",
                                  host="209.188.7.148",
                                  port="5432",
                                  database="data")
    cursor = connection.cursor()
    cursor.execute("select * from public.customers")
    DF = pd.DataFrame(cursor.fetchall())
    # Pushing a value to the context
    ti = kwargs['ti']
    ti.xcom_push(key='DFSize', value = DF.shape[0])

def python_fct2(**kwargs):
    ti = kwargs['ti']
    # Pulling a value from a Task - Depuis la tache Python_Task_1, avec Key x
    x = ti.xcom_pull(task_ids="Python_Task_1", key='DFSize')
    print("Customers DF Size is : " + str(x))

####### Definition des Operators #######

P1 = PythonOperator(
    task_id='Python_Task_1',
    python_callable=python_fct1,
    provide_context=True,
    dag=XYZ
)

P2 = PythonOperator(
    task_id='Python_Task_2',
    python_callable=python_fct2,
    provide_context=True,
    dag=XYZ
)



####### Definition des Etapes #######

P1 >> P2
