#!/bin/bash
set -e

bin/spark-submit --master local[2] --jars /root/project_kafka/spark-1.5.1-bin-hadoop2.6/spark-streaming-kafka-assembly_2.10-1.5.1.jar examples/src/main/python/streaming/run.py 192.168.99.100:2181 test

