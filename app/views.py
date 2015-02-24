"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from app import db
from app.models import User
from flask import jsonify, session
from datetime import *
from .forms import NewProfileForm
import json


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
  
# @app.route('/profile/')
# def profile():
#   """Render the profile page"""
#   return render_template('profile.html', date=timeinfo())

# import time
# def timeinfo():
#   """Return string with date formatted as specified"""
#   return "Today is: " + time.strftime("%a, %d %b, %Y")

@app.route('/profile/', methods=['POST', 'GET'])
def profile():
  """Render the profile page"""
  form = NewProfileForm()
  if form.validate_on_submit():
    #add user to db
    un = request.form['username']
    em = request.form['email']
    im = request.form['image']
    fn = request.form['fname']
    ln = request.form['lname']
    ag = int(request.form['age'])
    sx = request.form['sex']
    newUser = User(un, em, im, fn, ln, ag, sx)
    db.session.add(newUser)
    db.session.commit()
    nu = User.query.filter_by(username=un).first()
    return redirect('/profile/'+str(nu.id))
  return render_template('form.html', form=form)
#   if request.method == 'POST':
#     #add user to db
#     un = request.form['username']
#     em = request.form['email']
#     im = request.form['image']
#     fn = request.form['fname']
#     ln = request.form['lname']
#     ag = int(request.form['age'])
#     sx = request.form['sex']
#     newUser = User(un, em, im, fn, ln, ag, sx)
#     db.session.add(newUser)
#     db.session.commit()
#   else:
#     #serve form page
#     form = NewProfileForm()
#     return render_template('form.html', form=form)

import time
def timeinfo():
  """Return string with date formatted as specified"""
#   return "Today is: " + time.strftime("%a, %d %b, %Y")#need to alter to match postgres date fmt
  return datetime.now()

@app.route('/profile/<userid>', methods=['POST', 'GET'])
def user_profile(userid):
  usr = User.query.filter_by(id=userid).first()
  if request.method == 'POST':
    #return json
    return jsonify(id=usr.id, uname=usr.username, image=usr.image, sex=usr.sex, age=usr.age, highscore=usr.highscore, tdollars=usr.tdollars)
  else:
#     usr = User.query.filter_by(id=userid).first()
    user = {'id':usr.id, 'uname':usr.username, 'image':usr.image, 'age':usr.age, 'email':usr.email, 'fname':usr.fname, 'lname':usr.lname, 'sex':usr.sex, 'highscore':usr.highscore, 'tdollars':usr.tdollars}
    return render_template('userprofile.html', user=user)
  

@app.route('/profiles', methods=["POST", "GET"])
def profiles():
  users = db.session.query(User).all()
  if request.method == "POST":
    lst=[]
    for user in users:
      lst.append(jsonify(id=user.id, uname=user.username, image=user.image, sex=user.sex, age=user.age, highscore=user.highscore, tdollars=user.tdollars))
    return jsonify(users=lst)
  else:
    return render_template('profiles.html', users=users)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
