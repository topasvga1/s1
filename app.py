from flask import Flask
import os

app = Flask(__name__)

@app.app_context()
def setup():
    print("Application Setup Complete")

@app.route('/')
def hello():
    # 이 부분을 원하는 문구로 수정하세요!
    return """
    <h1>배포 테스트 성공! 🚀</h1>
    <p>현재 이 화면은 GitHub Actions를 통해 자동 배포되었습니다.</p>
    <p>버전: 2.0 (실시간 업데이트 확인용)</p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
