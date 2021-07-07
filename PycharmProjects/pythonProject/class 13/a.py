from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def default_page():
    # Well-Formed
    return render_template('index.html')
@app.route('/login',methods =['post','get'])
def login_page():
    return request.values['id']+','+request.values['name']
if __name__ == '__main__':
    #port = 8080
    app.run(debug=True,use_reloader = True)