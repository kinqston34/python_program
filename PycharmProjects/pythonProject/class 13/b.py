from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def default_page():
    print(request.headers)
    print(request.headers['User-Agent'])
    # Well-Formed
    return render_template('index.html')
@app.route('/login',methods =['post','get'])
def login_page():
    id = request.values['id']
    name = request.values['name']
    return render_template('result.html',id=id,name=name)
@app.route('/list')
def list_page():
    l = ['a','b','c']
    return render_template('index.html',x = l)
if __name__ == '__main__':
    #port = 8080
    app.run(debug=True,use_reloader = True)