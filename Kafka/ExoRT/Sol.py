from time import sleep
from json import dumps, loads
from random import choice
from kafka import KafkaProducer, KafkaConsumer, KafkaAdminClient

my_name = "Mehdi"

Admin = KafkaAdminClient(bootstrap_servers = ['209.188.7.148:9092'])
Admin.delete_topics([my_name])

producer = KafkaProducer(bootstrap_servers = ['209.188.7.148:9092'],
                         value_serializer = lambda v: dumps(v).encode('utf-8'))

receivers = ["Olivier", "Charlene", "Laurent", "Noura", "Malick", "Anne-Cha", "Pascal", "Zeyno", "Ludwig", "Tristan", "Camille"]
receiver = choice(receivers)
# receiver = "Laurent"
data = {'sender': my_name, 'message' : 'First Message'}
producer.send(receiver, value = data)
sleep(2)

consumer = KafkaConsumer(
     my_name,
     bootstrap_servers = ['209.188.7.148:9092'],
     auto_offset_reset = 'earliest',
     enable_auto_commit = True,
     value_deserializer = lambda x: loads(x.decode('utf-8')))


for message in consumer:
    message = message.value
    print('{} sent you : {}'.format(message['sender'], message['message'], ))
    reply = input("Reply : ")
    data = {'sender': my_name, 'message' : reply}
    producer.send(message['sender'], value = data)
    sleep(1)
