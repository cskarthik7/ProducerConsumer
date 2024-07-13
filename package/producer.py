import pika
from package.literals import QUEUE_NAME
from package.connections import establish_connection

def send_message_via_producer(message):
    channel, connection = establish_connection()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=message)
    print(f" PRODUCER: '{message}'")
    # Closing the connection
    connection.close()
