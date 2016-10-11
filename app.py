#!/usr/bin/python
from flask import Flask, render_template, request, sessions
import csv 

app = Flask(__name__)
APP.secret_key = '\xbc!<\xf2\x9eW1\rm\xc4=\xc8\x90b\x8d?iA\xdf\x98'



def auth():
   message = ""
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
    return message



@app.route('/')
    #if logged in 
    if len(session.keys()) != 0:  
        return redirect(url_for('welcome'))#already logged in
    else:
        return redirect(url_for('login'))


@app.route('/login/')
    render_template('login.html', message = "")


@app.route('/welcome/')
    render_template('welcome.html')


@app.route("/auth/", methods = ['POST'])
    def poe():
        x = auth()
    if (x == 'matches'):
        session['user'] = "yes"#logged in 
        redirect(url_for('welcome'))
    else: 
        render_template('login.html', message = x)


@app.route("/create/", methods = ['POST'])
    def lala():
        x = create()
    if (x == 'creation successful'):
        render_template('login.html', message = "account creation successful! you can try logging in now")
    else:
        render_template('login.html', message = x)






if __name__ == '__main__':
    app.run()
    app.debug = True
