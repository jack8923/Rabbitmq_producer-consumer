#!/usr/bin/env python
import pika, os, logging
from json_try import j_string,j_user,data
import json
logging.basicConfig()

body = json.dumps(data)

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')
params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='direct')

channel.basic_publish(exchange='', routing_key='direct', body=body)
print ("[x] Message sent to consumer")
connection.close()