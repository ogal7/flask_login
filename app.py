#!/usr/bin/python
from flask import Flask, render_template, request, session, redirect, url_for
import csv 

app = Flask(__name__)
app.secret_key = '\xbc!<\xf2\x9eW1\rm\xc4=\xc8\x90b\x8d?iA\xdf\x98'



def auth():
   #print request.form
   with open('logininfo.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if (request.form['user'] == row[0]):
                if (row[1] == request.form['pw']):
                    message = "matches"
                else:
                    message = "doesn't match"
            else:
                message = "doesn't exist"
        csvfile.close()
        return message

def create():
    #check if user already created
    with open('logininfo.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == request.form['Nuser']:
                csvfile.close()
                message = "this username has been taken"
    with open('logininfo.csv','w') as csvfile:
        info2Enter = [request.form['Nuser'],request.form['Npw']]
       #print info2Enter
        ww = csv.writer(csvfile)
        ww.writerow(info2Enter)
        message = "creation successful"
    csvfile.close()
    return message



@app.route('/')
def dipsy():
    if len(session.keys()) != 0:  
        return redirect(url_for('bigbird'))#already logged in
    else:
        return redirect(url_for('elmo'))


@app.route('/login/')
def elmo():
    return render_template('login.html', message = "")


@app.route('/welcome/')
def bigbird():
    return render_template('welcome.html')


@app.route('/logout/', methods = ['POST'])
def tinkiewinkie():
    session.pop('user')
    return redirect(url_for('elmo'))


@app.route("/auth/", methods = ['POST'])
def poe():
    x = auth()
    if (x == 'matches'):
        session['user'] = "yes"#logged in 
        return redirect(url_for('bigbird'))
    else: 
        return render_template('login.html', message = x)


@app.route("/create/", methods = ['POST'])
def lala():
    y = create()
    return render_template('login.html', message = y)


if __name__ == '__main__':
    app.run()
    app.debug = True
