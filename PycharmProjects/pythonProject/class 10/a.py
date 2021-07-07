from flask import Flask,render_template    #兩種方式 Django Flask
app = Flask(__name__)

@app.route('/')
def default_page():
    # Well-Formed
    return '<html><body>Hello</body></html>'
if __name__ == '__main__':
    app.run(debug=True,use_reloader = True,port = 8080)