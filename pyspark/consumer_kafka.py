# -*- coding:utf8 -*-

from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json

class Kafka_producer():
    '''
    使用Kafka模块
    '''

    def __init__(self,kafkahost,kafkaport,kafkatopic):
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkaTopic = kafkatopic
        self.producer = KafkaProducer(bootstrap_servers = '{kafka_host}:{kafka_port}'.format(
            kafka_host = self.kafkaHost,
            kafka_port = self.kafkaPort
        ))

    def sendJsondata(self,params):
        try:
            params_message = json.dumps(params)
            producer = self.producer
            print params_message
            producer.send(self.kafkaTopic,value=params_message.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            print e

class Kafka_consumer():
    '''
    使用Kafka-python的消费模块
    '''

    def __init__(self,kafkahost, kafkaport, kafkatopic, groupid):
        print "config pie"
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkatopic = kafkatopic
        self.groupid = groupid
        self.consumer = KafkaConsumer(self.kafkatopic, group_id = self.groupid,
                                      bootstrap_servers = '{kafka_host}:{kafka_port}'.format(
            kafka_host=self.kafkaHost,
            kafka_port=self.kafkaPort))

    def consumer_data(self):
        try:
            print "consumer_data"
            print self.consumer.config
            for message in self.consumer:
                yield message
        except KeyboardInterrupt as e:
            print e

def main():
    producer = Kafka_producer("hadoop-bd3",9092,"dyc")
    producer.sendJsondata('{"msg":"请求成功","code":1000,"data":[{"data":[{"date":"2017-10-27","value":1}],"name":"陕西"}]}')
    print "consumer start"
    consumer = Kafka_consumer('hadoop-bd3', 9092, "dyc", 'consumer_d')
    message = consumer.consumer_data()
    for i in message:
        print "consumer..."
        print i.topic,i.partition, i.offset, i.value

if __name__ == '__main__':
    main()