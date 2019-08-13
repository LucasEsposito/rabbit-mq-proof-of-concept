#!/usr/bin/env python
import pika
import time


def callback(channel, method, properties, body):
    print(f" [o] Received {body}")
    for i in range(1, 10):
        time.sleep(1)
        print(f'Processing: {i/10}%')
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print('ACK Sent')


# Set up the connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue in case it does not exist
channel.queue_declare(queue='hello')

# Set a function to consume on that queue
channel.basic_consume(queue='hello', on_message_callback=callback)
print(' [*] Waiting for messages. To exit press CTRL+C')

# Consume messages
channel.start_consuming()
