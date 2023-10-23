from chatPDF import app 
from flask import render_template, redirect, url_for
# from chatPDF.form import RegisterForm

@app.route('/')
@app.route('/home')
def home():  
    return render_template('home_chatbot.html')

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/sigin')
def sigin():
    return render_template('sigin.html')

@app.route('/baseuser')
def baseuser():
    return render_template('baseuser.html')


 