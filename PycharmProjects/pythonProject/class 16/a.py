from flask import Flask,render_template,jsonify
app = Flask(__name__)

@ app.route('/')
def home_page():
    dic = {'id':1,'name':'Mary'}
    #return jsonify(dic)
    #python -> JSON
    import json
    return json.dumps(dic)

if __name__ == "__main__":
    app.run(debug= True,use_reloader = True)