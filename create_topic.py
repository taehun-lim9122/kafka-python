from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaAdminClient

def create_topic(bootstrap_servers, topic_name, partitions, replication_factor):
    
    admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
    
    # 토픽 생성을 위한 NewTopic 객체 생성
    topic = NewTopic(name=topic_name,
                     num_partitions=partitions,
                     replication_factor=replication_factor)

    # 토픽 생성 요청
    admin_client.create_topics(new_topics=[topic], validate_only=False)
    print(f"토픽 '{topic_name}' 생성 완료")