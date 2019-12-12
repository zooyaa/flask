from flask import Flask, escape, request, render_template
# flask 모듈에서 Flask, escape, request 불러오기

app = Flask(__name__)

@app.route('/')     # 데코레이터(@) : 함수가 실행되기 전에 실행되는 부분    # 라우팅하기 위한 함수 route()   # '/' 경로 요청이 오면 아래 함수 실행
def hello():        # http://127.0.0.1:5000인 (경로)가 생략되어 있다고 생각할 것   # 라우팅 주소 매핑을 도와주는 함수(?)
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi')   # '/hi' 경로로 요청을 보내면 아래의 함수를 통해 응답
def hi():
    return 'hi'

@app.route('/zooya')   # http://127.0.0.1:5000/zooya 경로로 요청을 보내면
def zooya():           # zooya() 함수로 응답
    return 'Hello, zooya!'

@app.route('/html_tag')
def html_tag():
    return '<h1>안녕하세요</h1>'

@app.route('/html_file')
def html_file():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)     # .py 파일을 python hello.py 명령어로 실행시키기 위한 작업   # 자동으로 서버에 반영해주는 역할도 함