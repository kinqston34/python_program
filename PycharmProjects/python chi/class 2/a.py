from flask import Flask,render_template,request
# 建立 Flask 物件
app = Flask(__name__)
@app.route('/')
def default_page():
    print(request.headers)
    print(request.headers['User-Agent'])
    return render_template('index.html')
@app.route('/login',methods = ['get','post'])
def login():
    return render_template('result.html',id = request.values['id'],name = request.values['name'])

@app.route('/list')
def list_page():
    x = ['a','b','c']
    return render_template('index.html',l = x)
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)