from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <body style="text-align: center; padding-top: 50px; font-family: sans-serif;">
        <h1 style="color: #2e7d32;">🚀 배포 테스트 성공!</h1>
        <p>GitHub Actions를 통해 화면이 성공적으로 바뀌었습니다.</p>
        <div style="background: #f1f1f1; padding: 20px; display: inline-block; border-radius: 10px;">
            <strong>버전: 2.0 (Blue-Green/Canary 테스트 중)</strong>
        </div>
    </body>
    """

if __name__ == "__main__":
    # 포트가 Dockerfile/Service 설정과 일치하는지 확인 (보통 8080)
    app.run(host='0.0.0.0', port=8080)
