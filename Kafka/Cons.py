from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

consumer = KafkaConsumer(
    'messages',
     bootstrap_servers = ['209.188.7.148:9092'],
     auto_offset_reset = 'earliest',
     enable_auto_commit = True,
     group_id = 'my-group',
     value_deserializer = lambda x: loads(x.decode('utf-8')))


for message in consumer:
    message = message.value
    if message['receiver'] == "Mehdi":
        print('{}'.format(message))
