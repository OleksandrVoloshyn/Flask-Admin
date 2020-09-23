from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(Form):
    email = StringField('Email', [DataRequired(), Email()])
    password = StringField('Password', [DataRequired(), Length(4, 20, 'password must be 4-20 symbol')])
    login = SubmitField('Login')
