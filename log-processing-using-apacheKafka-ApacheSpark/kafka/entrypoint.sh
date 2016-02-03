#!/bin/bash
set -e

./zkServer.sh start &

cd /root/project_kafka/kafka_2.10-0.8.2.0
#gnome-terminal -e bin/kafka-server-start.sh config/server.properties & 
 bin/kafka-server-start.sh config/server.properties 
#gnome-terminal
#cd /root/project_kafka/kafka_2.10-0.8.2.0
#bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
#bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test 




