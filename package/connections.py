import pika

def establish_connection():
    parameters = pika.URLParameters('amqp://admin:password@localhost:5672/rabbit')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    return channel, connection