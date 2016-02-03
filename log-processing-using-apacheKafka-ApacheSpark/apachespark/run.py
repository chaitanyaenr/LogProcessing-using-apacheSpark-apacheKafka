

# Edited by Naga Ravi Chaitanya Elluri
from __future__ import print_function

import sys
import pprint
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: kafka_connect.py <zk> <topic>", file=sys.stderr)
        exit(-1)
    sc = SparkContext(appName="PythonStreamingKafkalogs")
    ssc = StreamingContext(sc, 1)

    zkQuorum, topic = sys.argv[1:]
    kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})
   # k= " ".join(kvs);
    errors=kvs.map(lambda c: c[1]).filter(lambda line: line.startswith("error"));
    #lines = kvs.map(lambda x: x[1])
    #counts = lines.flatMap(lambda line: line.split(" ")) \
      #  .map(lambda word: (word, 1)) \
       # .reduceByKey(lambda a, b: a+b) \
    #errors.collect()
    #kvs.pprint();
    errors.pprint();
    ssc.start()
    ssc.awaitTermination()


