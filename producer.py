
#   import os 
#   from slackclient import SlackClient
#   token = "xoxb-456010550053-478476771575-QwWRMkKl99HQcdIBKhQFJvdD"
#   slack_client = SlackClient(token)
#   bool = slack_client.rtm_connect(with_team_state=True)
# slack_client.api_call("chat.postMessage", channel="C0")
#Connect to slack
#   if bool:
    #   events = slack_client.rtm_read()

import logging
from faker import Faker
from confluent_kafka import Producer

def acked(err, msg):
    if err is not None:
        logging.error("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        logging.info("Message produced: {}".format(msg.value().decode("utf-8")))

myGen = Faker()

p = Producer({'bootstrap.servers': 'localhost:29092'})

try:
    while True:
        name = myGen.first_name()
        # print(name)
        p.produce('testtopic', name, callback=acked)
        p.poll(0.5)
except KeyboardInterrupt:
    pass

p.flush(30)



