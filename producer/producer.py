import logging
import random
import json
import uuid
import time
import arrow
from faker import Faker
from confluent_kafka import Producer

logging.basicConfig(format = '%(asctime)-12s %(levelname)-8s %(message)s',
                    datefmt = '%m-%d %H:%M', filename = '../test.log', filemode = 'w', level = logging.INFO)


p = Producer({'bootstrap.servers': 'lenrei-thinkpad-t480s.witt-ad.wittgruppe.eu:29092'})


def acked(err, msg):
    if err is not None:
        logging.error("Failed to deliver message: {0}: {1}"
                      .format(msg.value(), err.str()))
    else:
        logging.info("Message produced: {}".format(
            msg.value().decode("utf-8")))


myGen = Faker()


try:
    while True:
        value = {}
        key = uuid.uuid4()
        name = myGen.first_name()
        age = random.randint(18, 100)
        value["name"] = name
        value["age"] = age
        value["time"] = str(arrow.utcnow())
        p.produce('testnames', key = name, value = json.dumps(value), callback = acked)
        p.poll(0.5)
        time.sleep(5)
except KeyboardInterrupt:
    pass

p.flush(30)
