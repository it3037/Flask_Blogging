from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app=Flask(__name__)
app.config['SECRET_KEY']='63e274cf0a19aaef0d401369cde77b52'
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
