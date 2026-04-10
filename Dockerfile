# 1. 파이썬 실행 환경 설정
FROM python:3.9-slim

# 2. 컨테이너 내부 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 라이브러리 설치 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 전체 복사
COPY . .

# 5. 앱이 사용할 포트 명시
EXPOSE 8080

# 6. 앱 실행 명령어
CMD ["python", "app.py"]
