#!/usr/bin/python
from flask import Flask, render_template, request

app = Flask(__name__)
username = "ilovepugs123"
pw = "barbie"


@app.route('/')
def hello():
    return "hello"

@app.route('/login/')
def login():
    return render_template('login.html')



@app.route("/authenticate/", methods = ['POST'])

def auth():
   print request.form
   if (request.form['user'] == username and request.form['pw']== pw):
       return "congrats, your password worked"
   else:
       return "na u didn't remember ya password :( "

if __name__ == '__main__':
    app.run()
    app.debug = True
