from kafka.admin import KafkaAdminClient

def list_kafka_topics(bootstrap_servers):
    # KafkaAdminClient 생성
    admin_client = KafkaAdminClient(
        bootstrap_servers=bootstrap_servers
    )
    
    # 토픽 목록 가져오기
    topic_list = admin_client.list_topics()
    
    return topic_list

