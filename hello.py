#-*- coding: utf-8 -*-
 
# File Name: hello.py
# Author: Chris Xiong
# mail: 1050358918@qq.com
# Created Time: 2016-07-02 00:38
 
 
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/user/<name>')
def user_hello(name):
	return render_template('user.html',name=name)

app.run(debug=True)
