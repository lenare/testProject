import logging, queue
from confluent_kafka import Consumer, KafkaError

logging.basicConfig(filename = 'test.log', filemode = 'w', level = logging.INFO)

settings = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
}

c = Consumer(settings)

c.subscribe(['testtopic'])

names = {}

def name_to_dictionary(name):
    if name not in names:
        names[name] = 1
    else:
        names[name] += 1

def print_top_10_names(dict):
    print("top10")
    pq = queue.PriorityQueue()

    for name, count in dict.items():
        pq.put((-count, name))
    for i in range(1, 10):
        print("{0}. {1}".format(i, pq.get()))

try:
    while True:
        msg = c.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            name = msg.value().decode("utf-8")
            logging.info("Message received: {0}".format(name))
            name_to_dictionary(name)
            print(names)
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            logging.error('End of partition reached {0}/{1}'
                  .format(msg.topic(), msg.partition()))
            print_top_10_names(names)
        else:
            logging.error('Error occured: {0}'.format(msg.error().str()))

except KeyboardInterrupt:
    pass

finally:
    c.close()