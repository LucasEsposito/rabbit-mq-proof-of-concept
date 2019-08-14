# rabbit-mq-proof-of-concept

## About
This is a proof of concept designed only to learn rabbit-mq. It is not usable for any real use case and may not be the best implementation.

## How it works
- Different listeners choose a list of groups to subscribe to.
- A speakers send a message to a group.
- Then, all listener of that group will receive the message.

[[https://github.com/lucasesposito/rabbit-mq-proof-of-concept/blob/master/documentation/images/broadcast_usage_example.png]]