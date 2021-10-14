from flask import Flask,render_template,url_for
app=Flask(__name__)

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
def index():
  return render_template('home.html',posts=posts)

@app.route('/about')
def about():
  return render_template('about.html',title="About")

if __name__ == '__main__':
  app.run(debug=True)