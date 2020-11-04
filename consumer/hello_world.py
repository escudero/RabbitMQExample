import pika
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
  print(" [x] Received %r" % body)
  sleep(3)
  # print(dir(method))
  # Salvar no banco
  # Salvar no storage
  ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(
  queue='hello',
  # auto_ack=True,
  on_message_callback=callback
)

print(' [*] Waiting for messages. To exit press CTRL+C')
try:
  channel.start_consuming()
# except KeyboardInterrupt:
finally:
  channel.stop_consuming()
  print('Fnalizando...')




connection.close()