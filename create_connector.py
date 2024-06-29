import requests
import json

# Kafka Connect REST API 엔드포인트 URL
url = 'http://localhost:8083/connectors'

# 소스 커넥터의 설정 파일 경로
config_file = './scripts/classcimodels-employees-source-connector.json'

# 설정 파일을 읽어서 JSON으로 변환
with open(config_file, 'r') as f:
    connector_config = json.load(f)

# POST 요청 보내기
response = requests.post(url, headers={'Content-Type': 'application/json'}, json=connector_config)

print(response.status_code)
# 응답 확인
if response.status_code == 201:
    print('소스 커넥터가 성공적으로 생성되었습니다.')
else:
    print(f'소스 커넥터 생성 실패: {response.text}')
