import pika
from datetime import datetime
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

q = channel.queue_declare(queue='hello')

for i in range(20):
  msg = f'Send [{i}]: {datetime.now()}'
  channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=msg,
    properties=pika.BasicProperties(
        delivery_mode = 2, # make message persistent
    )
  )
  print(f" [x] {msg}")

try:
  for _ in range(10000):
    q = channel.queue_declare(queue='hello')
    c_count = q.method.consumer_count
    m_count = q.method.message_count
    print(f"[{c_count}] : {m_count}")
    sleep(0.5)
finally:
  connection.close()
  print('Fnalizando...')

