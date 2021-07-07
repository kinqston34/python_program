from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def default_page():
    # Well-Formed
    return render_template('index.html')
@app.route('/login')
def login_page():
    n = int(request.args.get('n'))
    if n % 2 == 0:
        return render_template('even.html')
    else:
        return render_template('odd.html')
if __name__ == '__main__':
    #port = 8080
    app.run(debug=True,use_reloader = True)