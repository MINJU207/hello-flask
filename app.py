from flask import Flask, request, render_template
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

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        keyword = request.form["keyword"]
        print(keyword)
        return f"POST로 전달된 당신이 입력한 검색어: {keyword}"

if __name__ == '__main__':
    app.run(host="0.0.0.0")