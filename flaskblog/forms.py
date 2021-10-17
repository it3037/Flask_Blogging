from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Email,Length,EqualTo
from flaskblog.models import User

class RegistrationForm(FlaskForm):
  username=StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
  email=StringField('Email', validators=[DataRequired(),Email()])
  password=PasswordField('Password', validators=[DataRequired()])
  confirm_password=PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
  submit=SubmitField('Sign Up')


  def validate_username(self,username):
    if True:
      raise ValidationError('Validation message')


class LoginForm(FlaskForm):
  email=StringField('Email', validators=[DataRequired(),Email()])
  password=PasswordField('Password', validators=[DataRequired()])
  remember=BooleanField('Remember Me')
  submit=SubmitField('Login')