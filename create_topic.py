from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaAdminClient, KafkaProducer

# Bootstrap 서버 설정
bootstrap_servers = ['localhost:9092','localhost:9093','localhost:9094']

# KafkaAdminClient 객체 초기화
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

def create_topic(topic_name, partitions, replication_factor):
    # 토픽 생성을 위한 NewTopic 객체 생성
    topic = NewTopic(name=topic_name,
                     num_partitions=partitions,
                     replication_factor=replication_factor)

    # 토픽 생성 요청
    admin_client.create_topics(new_topics=[topic], validate_only=False)
    print(f"토픽 '{topic_name}' 생성 완료")

# 토픽 생성 예제
if __name__ == "__main__":
    topic_name = "test-topic"
    partitions = 2
    replication_factor = 1
    create_topic(topic_name,partitions,replication_factor)
