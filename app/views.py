from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user
from app import app

from app.models import UserModel
from app.forms import LoginForm


@app.route('/')
def home():
    return redirect('admin')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        data = dict(request.form)
        del data['login']
        user = UserModel.query.filter_by(email=data['email']).first()
        if user and user.password == data['password']:
            login_user(user)
            return redirect(url_for('home'))
        return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
