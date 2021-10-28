from time import sleep
from json import dumps
from random import choice
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers = ['209.188.7.148:9092'],
                         value_serializer = lambda v: dumps(v).encode('utf-8'))

receivers = ["Olivier", "Charlene", "Laurent", "Noura", "Malick", "Anne-Cha", "Pascal", "Zeyno", "Ludwig", "Tristan", "Camille"]

message = input('Enter your message:')
data = {'sender': "Mehdi", 'receiver': choice(receivers), 'message' : message}
print('{}'.format(data))
producer.send('messages', value = data)
