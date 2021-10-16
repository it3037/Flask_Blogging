from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt

app=Flask(__name__)
app.config['SECRET_KEY']='63e274cf0a19aaef0d401369cde77b52'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/rakesh/Desktop/Flaskkk/Flask_Blogging/flaskblog/site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskblog import routes
