import pika
import json
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

message = {
    'text': 'Salut IDEMIA!',
    'timestamp': datetime.datetime.now().isoformat()
}

channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=json.dumps(message)
)

print("[x] Sent:", message)
connection.close()
