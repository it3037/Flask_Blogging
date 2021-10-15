from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app=Flask(__name__)


app.config['SECRET_KEY']='63e274cf0a19aaef0d401369cde77b52'

posts = [
  {
    'author': 'raka',
    'title': 'blogging',
    'content': 'first post about blogging',
    'date_posted': 'Oct 14 , 2021'
  },
  {
    'author': 'chikku',
    'title': 'blogging',
    'content': 'first post about blogging',
    'date_posted': 'Oct 14 ,2022'
  }
]

@app.route('/')
def home():
  return render_template('home.html',posts=posts)

@app.route('/about')
def about():
  return render_template('about.html',title="About")


@app.route('/register',methods=['POST','GET'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!','success')
    return redirect(url_for('home'))
  return render_template('register.html',title="Register",form=form)

@app.route('/login')
def login():
  form = LoginForm()
  return render_template('login.html',title="Login",form=form)

if __name__ == '__main__':
  app.run(debug=True)