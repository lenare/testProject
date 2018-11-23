# testProject

This is a test project to learn how to use Kafka and KSQL.

## How to set up Kafka and the KSQL-CLI:

- Clone the following github repository: https://github.com/confluentinc/cp-docker-images
- `cd` into cp-docker-images/examples/cp-all-in-one
- Start the docker container with `docker-compose up [-d]`
- In a new terminal execute 
    `docker exec -it <id of ksql-cli container> /bin/sh`
- `#` appears and type `ksql`
- Change server of the ksql-cli with 
    `server http://ksql-server:8088`
- Now you can enter any KSQL commands

