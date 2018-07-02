#-*- coding: utf-8 -*-
from flask import Flask,render_template,request,jsonify
from reset_pwd import reset_pwd

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_AS_ASCII'] = False

@app.route('/get/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        info = request.form.get('info')
        return jsonify(reset_pwd(info))

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)
