#!/usr/bin/python
# Author: Scott Iwako
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
from flask import url_for
from flask import flash
from flask import session as login_session
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Coffee, Origin

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///coffee.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/home')
def showHomePage():
    origins = session.query(Origin).all()
    coffees = session.query(Coffee).all()
    return render_template('main.html', origins=origins, coffees=coffees)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
