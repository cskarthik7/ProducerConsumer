import pika
from .literals import QUEUE_NAME
from .connections import establish_connection

def callback(ch, method, properties, body):
    print(f" CONSUMER: Received {body}")

def start_consumer():
    channel, _ = establish_connection()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

#start_consumer()
