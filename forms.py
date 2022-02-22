from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class EmailPasswordForm(FlaskForm):
    email_name = StringField('spokoj@gmail.com', validators=[DataRequired(), Email()])
    password = StringField('okej', valdators=[DataRequired()])