#!/usr/bin/env python
import pika
import argparse


def callback(channel, method, properties, body):
    print(f" [x] Broadcast from group {method.routing_key}: {body.decode('utf-8')}")


# Parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument("-groups-to-watch", help="Numbers of the groups to subscribe. Use comma as separator.")
args = parser.parse_args()
args.groups_to_watch = [group.strip() for group in args.groups_to_watch.split(',')]

# Set up the connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='message_queue'))
channel = connection.channel()
channel.exchange_declare(exchange='chat_exchange', exchange_type='direct')
channel.basic_qos(prefetch_count=1)  # to not receive more than one message at a time.


# Listen only to the groups received by parameter, using one routing key for each one
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
for group in args.groups_to_watch:
    print(f'Subscribed to group: {group}')
    channel.queue_bind(exchange='chat_exchange', queue=queue_name, routing_key=group)

# Consume messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
