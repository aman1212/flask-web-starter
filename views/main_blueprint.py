from flask import Blueprint, render_template, request, session,redirect, flash
from models.model import User
from lib.helpers import timecheck
from datetime import datetime,timedelta
import hashlib

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/')
def index():
    return render_template('home.html')
@main_blueprint.route('/home')
def home():
    return render_template('home.html')
@main_blueprint.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'pass' in request.form:\
        # Create variables for easy access
        email = request.form['email']
        password = request.form['pass']

        u = User()
        u.email = email
        u.password = hashlib.md5((password + "aman is the best").encode()).hexdigest()

        session['login'] = False
        if(u.aut()):
            if(u.stat == 'act'):
                session['login'] = True
                session['user'] = u.toJSON()
                session['time'] = datetime.now() + timedelta(hours=1)
                return redirect('/dashbord')
            else:
                return render_template('index.html',msg="User Not Active")
        else:
            return render_template('index.html',msg="email or password not correct")
    if(timecheck()):
        return redirect('/dashbord')
    return render_template('index.html')
@main_blueprint.route('/regster', methods =['GET', 'POST'])
def regster():
    if request.method == 'POST':
        return render_template('index.html')
    return render_template('index.html')

@main_blueprint.route('/logout')
def logout():
    session['login'] = False
    session.pop('user',None)
    session.pop('time',None)
    return redirect('/login')

@main_blueprint.route('/dashbord')
def dashbord():
    if(timecheck()):
       return render_template('dashbord.html',user=session['user'])
    else:
       flash('You have to login first')
       return redirect('/login')

        