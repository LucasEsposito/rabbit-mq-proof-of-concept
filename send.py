#!/usr/bin/env python
import pika
import sys

# Set up the connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue in case it does not exist
channel.queue_declare(queue='hello')

# Send parameters as a single message
channel.basic_publish(exchange='', routing_key='hello', body=' '.join(sys.argv[1:]))
print(f" [x] Message sent.'")

# Close the connection
connection.close()
