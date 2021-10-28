from kafka import KafkaProducer
from json import dumps
from time import sleep
import psycopg2

connection = psycopg2.connect(user="postgres",
                                password="123456789",
                                host="209.188.7.148",
                                port="5432",
                                database="data")
cursor = connection.cursor()
cursor.execute("select * from public.customers")

producer = KafkaProducer(bootstrap_servers = ['209.188.7.148:9092'],
                         value_serializer = lambda v: dumps(v).encode('utf-8'))
# fetchone is used to get line by line from PGSQL
# row = cursor.fetchone()
row = cursor.fetchone()
while row is not None:
    data = {'ID': row[0], 'DOB': row[1], 'Gender': row[2], 'City': row[3]}
    producer.send('customers', value = data)
    row = cursor.fetchone()
    sleep(1)
