from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'Groupe Data',
    'start_date': datetime.now()
}

XYZ = DAG('data_exo_1', default_args=default_args)

####### Definition des Fonctions / Executions #######

def python_fct1():
    now = datetime.now()
    print("Task 1 : " + str(now))

def python_fct2():
    now = datetime.now()
    print("Task 2 : " + str(now))

def python_fct3():
    now = datetime.now()
    print("Task 3 : " + str(now))

####### Definition des Operators #######

P1 = PythonOperator(
    task_id='Python_Task_1',
    python_callable=python_fct1,
    dag=XYZ
)

P2 = PythonOperator(
    task_id='Python_Task_2',
    python_callable=python_fct2,
    dag=XYZ
)

P3 = PythonOperator(
    task_id='Python_Task_3',
    python_callable=python_fct3,
    dag=XYZ
)


####### Definition des Etapes #######

P1 >> [P2, P3]
