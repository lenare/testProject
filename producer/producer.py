import logging
from faker import Faker
from confluent_kafka import Producer

logging.basicConfig(format = '%(asctime)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M', filename = '../test.log', filemode = 'w', level = logging.INFO)


def acked(err, msg):
    if err is not None:
        logging.error("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        logging.info("Message produced: {}".format(msg.value().decode("utf-8")))

myGen = Faker()

settings = {
    'bootstrap.servers': 'lenrei-thinkpad-t480s.witt-ad.wittgruppe.eu:29092',
    'group.id': 'mygroup',
    'client.id': 'client-2',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
}

p = Producer(settings)

print("blubb")

try:
    while True:
        name = myGen.first_name()
        # print(name)
        p.produce('testtopic', key = "test_key", value = name, callback=acked)
        p.poll(0.5)
except KeyboardInterrupt:
    pass

p.flush(30)

