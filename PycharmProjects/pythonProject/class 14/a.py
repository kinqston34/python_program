# control.py
from flask import Flask,render_template,request
app = Flask(__name__)
# def add(a,b):
#     return a+b
@ app.route('/')
def home_page():
    return render_template('home.html')
@ app.route('/add',methods = ['get','post'])
def add_page():
    a = int(request.values['a'])
    b = int(request.values['b'])
    return str(a+b)
    # return render_template('add_result.html',ans = ans)
if __name__ == "__main__":
    app.run(debug= True,use_reloader = True)