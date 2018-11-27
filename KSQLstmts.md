# KSQL Statements for testProject

### Show Topics/Streams/Tables:

    SHOW TOPICS/STREAMS/TABLES;

### Show entries:
    SELECT * FROM <name of stream or table>;

### Create Stream:
    CREATE STREAM namestream (name VARCHAR, age BIGINT) WITH (KAFKA_TOPIC='testnames', VALUE_FORMAT='JSON'[, KEY='name']);

### Create Table:
    CREATE TABLE namestable (name VARCHAR, age BIGINT) WITH (KAFKA_TOPIC='testnames', VALUE_FORMAT='JSON', KEY='name');
