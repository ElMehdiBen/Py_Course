from time import sleep
from json import dumps
from random import choice
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers = ['209.188.7.148:9092'],
                         value_serializer = lambda v: dumps(v).encode('utf-8'))

receivers = ["Olivier", "Charlene", "Laurent", "Noura", "Malick", "Anne-Cha", "Pascal", "Zeyno", "Ludwig", "Tristan", "Camille"]

for e in range(1000):
    data = {'sender': "Mehdi", 'receiver': choice(receivers), 'number' : e}
    print('{}'.format(data))
    producer.send('messages', value = data)
    sleep(3)
