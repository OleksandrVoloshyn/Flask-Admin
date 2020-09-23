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
            return redirect(url_for('login_u', user_id=user.id))
        return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/login_user/<user_id>')
def login_u(user_id):
    user = UserModel.query.get(user_id)
    # Коли передавав юзера з функції логін вибиває помилку
    login_user(user)
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
