from kafka import KafkaConsumer
from json import loads
import psycopg2

connection = psycopg2.connect(user="postgres",
                                password="123456789",
                                host="209.188.7.148",
                                port="5432",
                                database="data")
cursor = connection.cursor()

consumer = KafkaConsumer(
    'customers',
     bootstrap_servers = ['209.188.7.148:9092'],
     auto_offset_reset = 'earliest',
     enable_auto_commit = True,
     value_deserializer = lambda x: loads(x.decode('utf-8')))

INSERT = """INSERT INTO public.customers_new(
	customer_id, dob, gender, city_code)
	VALUES (%s,%s, %s, %s);"""

for message in consumer:
    message = message.value
    cursor.execute(INSERT, (message['ID'], message['DOB'], message['Gender'], message['City']))
    connection.commit()
    print('{}'.format(message))
