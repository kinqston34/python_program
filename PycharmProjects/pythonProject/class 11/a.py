from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def default_page():
    # Well-Formed
    return render_template('index.html')
if __name__ == '__main__':
    #port = 8080
    app.run(debug=True,use_reloader = True)