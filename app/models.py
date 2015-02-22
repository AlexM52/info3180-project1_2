from . import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  image = db.Column(db.String(50))
  fname = db.Column(db.String(40))
  lname = db.Column(db.String(40))
  age = db.Column(db.Integer)
  sex = db.Column(db.String(6))
  highscore = db.Column(db.Integer)
  tdollars = db.Column(db.Integer)#float type?
  
  def __init__(self, username, email):
    self.username = username
    self.email = email
    self.image = image
    self.fname = fname
    self.lname = lname
    self.age = age
    self.sex = sex
    self.highscore = highscore
    self.tdollars - tdollars

  def __repr__(self):
    return '<User %r>' % self.username