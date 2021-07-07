from flask import Flask,render_template,request,jsonify
# 建立 Flask 物件
app = Flask(__name__)
@app.route('/')
def default_page():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True,port=8080)