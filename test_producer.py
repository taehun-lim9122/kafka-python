from kafka import KafkaProducer
from json import dumps
import time

from check_topic_list import list_kafka_topics
from create_topic import create_topic

from datetime import datetime
import pytz

def test_producer():
    bootstrap_servers = ['localhost:9092','localhost:9093','localhost:9094']
    topic_name = 'test-topic'
    partitions = 2
    replication_factor = 1
    
    producer = KafkaProducer(
        acks=0, # 메시지 전송 완료에 대한 체크
        compression_type='gzip', # 메시지 전달할 때 압축(None, gzip, snappy, lz4 등)
        bootstrap_servers = bootstrap_servers,
        value_serializer=lambda x:dumps(x).encode('utf-8') # 메시지의 값 직렬화
    )
    
    topic_list = list_kafka_topics(bootstrap_servers)
    
    if topic_name in topic_list:
        print('토픽 있어요')
    else:
        print('토픽 없어여')
        create_topic(bootstrap_servers, topic_name, partitions, replication_factor)
    
    try:
        while True:
            now = datetime.now()
            ko_timezone = pytz.timezone('Asia/Seoul')
            ko_time = now.astimezone(ko_timezone)
            ko_time_format = ko_time.strftime('%Y-%m-%d %H:%M:%S')
            
            ny_timezone = pytz.timezone('UTC')
            ny_time = now.astimezone(ny_timezone)
            ny_time_format = ny_time.strftime('%Y-%m-%d %H:%M:%S')
            
            message_1 = {'key': 'KST', 'timestamp': ko_time_format}
            message_2 = {'key': 'UTC', 'timestamp': ny_time_format}
            
            producer.send(topic_name, message_1)
            producer.send(topic_name, message_2)
            
            print(f"Sent: {message_1}")
            print(f"Sent: {message_2}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        producer.close()

    
test_producer()