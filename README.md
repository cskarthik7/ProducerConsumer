# RabbitMQ Producer-Consumer System

This guide outlines how to set up a RabbitMQ messaging system using Docker and Python, with examples of running both a producer and a consumer.

## Prerequisites

Make sure you have the following installed:

- Docker
- Python 3.x

## Setting Up RabbitMQ with Docker

1. Pull the RabbitMQ Docker image with management plugin

   ```bash
   docker pull rabbitmq:3-management

2. Install required packages

   ```bash
   pip install -r requirements.txt


3. Run RabbitMQ container with management plugin enabled

   ```bash
   docker run -d --name rabbitmq-pika -p 5672:5672 -p 25672:15672 -v ./build/rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf rabbitmq:3-management

4. To start producer

   ```bash
   python3 main.py --start_producer

5. To start consumer

   ```bash
   python3 main.py --start_consumer

