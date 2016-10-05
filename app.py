#!/usr/bin/python
from flask import Flask, render_template, request
import csv 

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello"

@app.route('/login/')
def login():
    return render_template('login.html')



@app.route("/authenticate/", methods = ['POST'])

def auth():
   #print request.form
   with open('logininfo.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if (request.form['user'] == row[0]):
                if (row[1] == request.form['pw']):
                    return "your login info matches, good job"
                else:
                    return "your stuff does not match mi amigo"
            else:
                return "that username is not recognized by dis fire ass system"


@app.route("/create/", methods = ['POST'])
def create():
    #check if user already created
    with open('logininfo.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == request.form['user']:
                csvfile.close()
                return "this username has been taken"
    with open('logininfo.csv','w') as csvfile:
        info2Enter = [request.form['user'],request.form['pw']]
        print info2Enter
        ww = csv.writer(csvfile)
        ww.writerow(info2Enter)
        return "creation successful"
    return "ok"


if __name__ == '__main__':
    app.run()
    app.debug = True
