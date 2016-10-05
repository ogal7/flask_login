#!/usr/bin/python
from flask import Flask, render_template, request
import csv 

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


@app.route("/create/", methods = ['POST'])
def create():
    #check if user already created
    with open('logininfo.csv', r) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if (request.form['user'] == row[0]):
                return "this username has already been taken!"
            else:
                with open('logininfo.csv', w) as csvfile:
                    info2Enter = request.form['user'] + "," + request.form['pw']
                    csvwriter.writerow(info2Enter)

if __name__ == '__main__':
    app.run()
    app.debug = True
