# example_consumer.py
import pika, os
import json

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='direct')


def callback(ch, method, properties, body):
  data = json.loads(body)
  print(" [x] Received ")
  print("ID: {}".format(data['orderId']))
  print("Products {}".format(data['products']))
  print('Receipient {}'.format(data['receipient']))


channel.basic_consume('direct',callback,auto_ack=True)


channel.start_consuming()
connection.close()

# export PATH=$PATH:/usr/local/opt/rabbitmq/sbin
