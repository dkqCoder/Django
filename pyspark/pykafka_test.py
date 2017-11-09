# -*- coding:utf8 -*-

from pykafka import KafkaClient

class kafka_consumer():
    def consumer(self,topicname):
        client = KafkaClient(hosts='hadoop-bd1:9092,hadoop-bd2:9092,hadoop-bd3:9092,hadoop-bd4:9092,hadoop-bd5:9092')
        topic = client.topics[topicname]
        balanced_consumer = topic.get_balanced_consumer(
            consumer_group='consumer_k',
            auto_commit_enable=True,
            reset_offset_on_start = True,
            auto_offset_reset = 100,
            zookeeper_connect='hadoop-bd1:2181,hadoop-bd2:2181,hadoop-bd3:2181,hadoop-bd4:2181,hadoop-bd5:2181'
        )
        for message in balanced_consumer:
            if message is not None:
                print message.partition.id, message.offset , message.value

class kafka_producer():
    def producer(self,topicname,message):
        client = KafkaClient(hosts='hadoop-bd1:9092,hadoop-bd2:9092,hadoop-bd3:9092,hadoop-bd4:9092,hadoop-bd5:9092')
        topic = client.topics[topicname]

        with topic.get_sync_producer() as producer:
            producer.produce(message)

def main():
    k_consumer = kafka_consumer()
    k_consumer.consumer('dyc')
    # k_producer = kafka_producer()
    # k_producer.producer('dyc',"test message test message")

if __name__ == '__main__':
    main()