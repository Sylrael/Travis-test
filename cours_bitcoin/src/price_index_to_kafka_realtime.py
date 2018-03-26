# priceIndexToKafkaRealtime.py

import requests
import time
from kafka import SimpleProducer, KafkaClient

# Connect to Kafka
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)

# Assign a topic
topic = 'bitcoin-realtime'

# Send message
while 1:
    jsonFile = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    producer.send_messages(topic, str(jsonFile.text))
    time.sleep(45)
