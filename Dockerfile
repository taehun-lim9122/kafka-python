FROM python:3.8.18

WORKDIR /app

# requirements.txt 파일을 컨테이너에 복사
COPY requirements.txt .

# requirements.txt 파일을 사용하여 라이브러리 설치
RUN pip install --no-cache-dir -r requirements.txt

# producer 폴더를 컨테이너에 복사
COPY . .

CMD ["python", "create_topic.py"]


# CMD 명령어는 docker-compose.yml에서 정의
