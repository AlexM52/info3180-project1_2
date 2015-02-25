from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/project1_2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nuvvubrysbqmrz:QjhlkvAnHI8QY_RETj76R8Q63-@ec2-23-21-219-209.compute-1.amazonaws.com:5432/d8rqq5trvho033'
db = SQLAlchemy(app)

from app import views, models

WTF_CSRF_ENABLED = False