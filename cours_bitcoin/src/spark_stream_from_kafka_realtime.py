import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
import json
from elasticsearch import Elasticsearch
from datetime import datetime

# Initialize sparkSession
spark = SparkSession \
    .builder \
    .appName("SparkStreamKafka") \
    .config("master", "local[2]") \
    .getOrCreate()
# Retrieve sparkContext from session
sc = spark.sparkContext

#Default values
broker = 'localhost:9092'
topic = 'bitcoin-realtime'
host_es = 'localhost'
port_es = '9200'
currency = 'EUR'

# Input values
if (len(sys.argv) >= 3):
	broker = sys.argv[1]
	topic = sys.argv[2]
if (len(sys.argv) >= 5):
	host_es = sys.argv[3]
	port_es = sys.argv[4]
if (len(sys.argv) >= 6):
	currency = sys.argv[5]

def addElastic(jsonObject):
    date = datetime.strptime(jsonObject["time"]["updated"], "%b %d, %Y %H:%M:%S %Z")
    rate = jsonObject["bpi"][currency]["rate_float"]
    devise = jsonObject["bpi"][currency]["code"]
    es = Elasticsearch([{'host': host_es, 'port': port_es}])
    es.index(index='cours_btc_idx', doc_type='cours_btc', id=date, body={'date': date, 'rate': rate, 'devise': devise, 'data_type': 'temps_reel'})


def sendData(tuple):
    text = tuple[1].encode("utf-8")
    jsonObj = json.loads(text)
    print (jsonObj["time"]["updated"])
    print (jsonObj["bpi"][currency]["rate"])
    print (jsonObj["bpi"][currency]["code"])

    addElastic(jsonObj)


def sendDataToElastic(rdds):
     rdds.foreach(lambda rdd: sendData(rdd))


def main():

    ssc = StreamingContext(sc, 10)

    #broker, topic = sys.argv[3:]

    kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": broker})

    kvs.foreachRDD(sendDataToElastic)

    ssc.start()
    ssc.awaitTermination()


if __name__ == "__main__":
    main()
