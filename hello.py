from flask import Flask, escape, request, render_template
# flask 모듈에서 Flask, escape, request 불러오기
import random

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
    return render_template('index.html')    # render_template() 함수

@app.route('/variable')
def variable():
    name = "yogi"
    return render_template('variable.html', html_name=name)

@app.route('/greeting/<string:name>/')
def greeting(name):
    def_name = name
    return render_template('greeting.html', html_name=def_name)

@app.route('/cube/<int:number>/')
def cube(number):
    cube = number ** 3
    return render_template('cube.html', number=number, cube=cube)

@app.route('/lunch')
def lunch():
    # menu_dic = {
    #     "sandwich" : "https://realfood.tesco.com/media/images/RFO-1400x919-ChickenClubSandwich-0ee77c05-5a77-49ac-a3bd-4d45e3b4dca7-0-1400x919.jpg",
    #     "pad thai" : "https://www.washingtonpost.com/rf/image_982w/2010-2019/WashingtonPost/2019/05/21/Food/Images/v-essentials-padthai_08-001.jpg",
    #     "galbi" : "http://media.foodnetwork.ca/recipetracker/ce9180e1-7dee-4826-b6e3-69bded15310e_anju03_WebReady.jpg"
    # }
    # menu_list = list(menu.keys())
    # menu = random.choice(menu_list)
    # img = menu_dic[menu]
    # return render_template('lunch.html', menu=menu, img=img)
    menu_list = ["sandwich", "pad thai", "galbi"]
    # menu = random.sample(menu_list, 1)[0]
    menu = random.choice(menu_list)
    if menu == menu_list[0]:
        img = "https://realfood.tesco.com/media/images/RFO-1400x919-ChickenClubSandwich-0ee77c05-5a77-49ac-a3bd-4d45e3b4dca7-0-1400x919.jpg"
    elif menu == menu_list[1]:
        img = "https://www.washingtonpost.com/rf/image_982w/2010-2019/WashingtonPost/2019/05/21/Food/Images/v-essentials-padthai_08-001.jpg"
    else:
        img = "http://media.foodnetwork.ca/recipetracker/ce9180e1-7dee-4826-b6e3-69bded15310e_anju03_WebReady.jpg"
    return render_template('lunch.html', menu=menu, img=img)

@app.route('/movies')
def movies():
    movies = ["겨울왕국2", "쥬만지", "감쪽같은 그녀"]
    return render_template('movies.html', movies=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong', methods=['GET', 'POST'])
def pong():
    # request.args => GET방식으로 데이터가 들어오는 경우
    # keyword = request.args.get('keyword')
    # print(request.form.get('keyword'))
    keyword = request.form.get('keyword')
    return render_template('pong.html', keyword=keyword)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

if __name__ == "__main__":
    app.run(debug=True)     # .py 파일을 python hello.py 명령어로 실행시키기 위한 작업   # 자동으로 서버에 반영해주는 역할도 함