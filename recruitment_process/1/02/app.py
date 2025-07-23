
from flask import Flask

# Flask 애플리케이션 인스턴스를 생성합니다.
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, DevOps!"

if __name__ == "__main__":
    # Flask 애플리케이션을 0.0.0.0 호스트와 8080 포트에서 실행한다.
    # host='0.0.0.0'은 모든 공개 IP에서 접속을 허용한다.
    # port=8080은 애플리케이션이 8080 포트에서 수신 대기하도록 설정한다.
    app.run(host='0.0.0.0', port=8080)