from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/test'
db = SQLAlchemy(app)

from app import views, models

WTF_CSRF_ENABLED = False