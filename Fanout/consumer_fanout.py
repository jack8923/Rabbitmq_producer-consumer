import pika, os, time
import json

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

channel.queue_declare(queue='queue1')
channel.queue_declare(queue='queue2')

channel.queue_bind(exchange='logs', queue='queue1')
channel.queue_bind(exchange='logs', queue='queue2')

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(" [x] Received ")
    print("ID: {}".format(data['orderId']))
    print("Products {}".format(data['products']))
    print('Receipient {}'.format(data['receipient']))

    time.sleep(5)


channel.basic_consume('queue1', callback, auto_ack=True)
channel.basic_consume('queue2', callback, auto_ack=True)

channel.start_consuming()
