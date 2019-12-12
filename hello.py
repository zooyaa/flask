from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == "__main__":
    app.run(debug=True)     # .py 파일을 python hello.py 명령어로 실행시키기 위한 작업