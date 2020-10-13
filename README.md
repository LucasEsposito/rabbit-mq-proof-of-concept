# rabbit-mq-proof-of-concept

## About
This is a proof of concept designed only to learn rabbit-mq. It works, but it was not designed for any real use case. I aimed to try out different rabbit-mq features. The implmenetation may not be the best regarding programming practices, as this is not a real program by any mean.

## How it works
- Different listeners choose a list of groups to subscribe to.
- A speakers send a message to a group.
- Then, all listeners of that group are going to receive the message.

![broadcast_usage_example](https://github.com/lucasesposito/rabbit-mq-proof-of-concept/blob/master/documentation/images/broadcast_usage_example.png?raw=true "Broadcast usage example")
