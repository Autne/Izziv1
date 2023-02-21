import requests, string
from flask import Flask, render_template, request, redirect

app = Flask('app')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/getPass')
def password():
  pwd_len = request.args["pass"]
  print(pwd_len)
  return "A"*int(pwd_len)
  #return render_template('password.html')

app.run(host='0.0.0.0', port=8080)