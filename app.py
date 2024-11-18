from flask import Flask, request, render_template
import nvapi

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/baseball')
def baseball():
    return 'Hello, baseball!'

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ytpage')
def ytpage():
    return render_template('ytpage.html')

@app.route('/youtube', methods=['GET', 'POST'])
def youtube():
    linklist = ['https://www.youtube.com/embed/wsk95Mq0Cys?si=wdVWrmJJY7hnX-c0', 'https://www.youtube.com/embed/z6TgbMB4mms?si=E6VMYPWjARq_a-mj']
    keyword = request.form["keyword"]
    print(keyword)
    linknum = 0 # 0은 이영지,  1은 임영웅
    if keyword == '이영지':
        linknum = 0
    elif keyword == '임영웅':
        linknum = 1
    else:
        print('잘못된입력')
    return render_template('youtube.html', name=keyword, link=linklist[linknum])

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        keyword = request.form["keyword"]
        print(keyword)
        data = nvapi.blog(keyword)
        # return f"POST로 전달된 당신이 입력한 검색어: {keyword}"
        return render_template("result.html", keyword=keyword, blist=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0")