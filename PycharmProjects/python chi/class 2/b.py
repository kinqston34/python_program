from flask import Flask,render_template,request
# 建立 Flask 物件
app = Flask(__name__)
@app.route('/')
def default_page():
    return render_template('index_2.html')
def add(a,b):
    return a+b
@app.route('/add',methods = ['post'])
def add_page():
    a = int(request.values['a'])
    b = int(request.values['b'])
    # return str(a+b)
    return str(add(a,b))
import unittest
class MTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add(1,2),3)
if __name__ == '__main__':
    #app.run(debug=True, use_reloader=True,port=8080)
    unittest.main()