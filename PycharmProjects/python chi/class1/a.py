from flask import Flask,render_template,request
# 建立 Flask 物件
app = Flask(__name__)
@app.route('/')
def default_page():
    return render_template('index.html')
@app.route('/login',methods = ['get','post'])
def login():
    #return request.form.get('id') + "," + request.form.get('name')   #method = "post" in html
    #request.args.get('id') + ',' + request.args.get('name')   #method = "get" in html
    return request.values['id'] + ',' + request.values['name'] #get post 都收的到
if __name__ == '__main__':
    app.run(debug = True,use_reloader = True)
