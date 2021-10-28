from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers = ['209.188.7.148:9092'],
                         value_serializer = lambda v: dumps(v).encode('utf-8'))

for e in range(1000):
    data = {'number' : e}
    producer.send('numtest', value = data)
    sleep(5)
