#!/usr/bin/env python
import pika
import argparse

# Parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument("-receiver-group", help="Number of the group to broadcast to.")
parser.add_argument("-message", help="Message to send.")
args = parser.parse_args()


# Set up the connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='message_queue'))
channel = connection.channel()

# Declare the queue in case it does not exist
channel.exchange_declare(exchange='chat_exchange', exchange_type='direct')
# channel.queue_declare(queue='hello', durable=True)

# Send message
channel.basic_publish(exchange='chat_exchange',
                      routing_key=args.receiver_group,
                      body=args.message)
print(f" [x] Message '{args.message}' sent to group '{args.receiver_group}'.")

# Close the connection
connection.close()
