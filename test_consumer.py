from kafka import KafkaConsumer, TopicPartition
import threading

bootstrap_servers = ['localhost:9092','localhost:9093','localhost:9094']
topic_name = 'test-topic'

def consume_partition(partition):
    consumer = KafkaConsumer(
        bootstrap_servers=bootstrap_servers,
        group_id='consumer-group-test',  # 컨슈머 그룹 ID
        auto_offset_reset='earliest',  # 가장 처음부터 메시지를 가져올 수 있도록 설정
        enable_auto_commit=True,  # 자동 커밋 활성화
    )
    consumer.assign([TopicPartition(topic_name, partition)])

    try:
        while True:
            for message in consumer:
                print(f"Consumer {partition+1} (Partition {partition}) - Received message: {message.value.decode('utf-8')}")

    except KeyboardInterrupt:
        print(f"Consumer {partition+1} (Partition {partition}) - Interrupted, closing consumer...")
    finally:
        consumer.close()

partition0_consumer_thread = threading.Thread(target=consume_partition, args=(0,))
partition1_consumer_thread = threading.Thread(target=consume_partition, args=(1,))

partition0_consumer_thread.start()
partition1_consumer_thread.start()

partition0_consumer_thread.join()
partition1_consumer_thread.join()

print("All consumers finished.")
