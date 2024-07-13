from package.consumer import start_consumer
from package.producer import send_message_via_producer
import argparse

def main():
    parser = argparse.ArgumentParser(description='RabbitMQ Producer Example')
    parser.add_argument('--start_producer', action='store_true', help='Start the RabbitMQ producer')
    parser.add_argument('--start_consumer', action='store_true', help='Start the RabbitMQ producer')

    args = parser.parse_args()

    if args.start_producer:
        send_message_via_producer(message="Sending message to RabbitMQ")

    if args.start_consumer:
        start_consumer()


if __name__ == '__main__':
    main()