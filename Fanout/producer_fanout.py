#!/usr/bin/env python
import pika, os, logging
from json_try import data
import json

logging.basicConfig()

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')
params = pika.URLParameters(url)

body = json.dumps(data)

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = body
channel.basic_publish(exchange='logs', routing_key='', body=message)
print("SENT")
connection.close()