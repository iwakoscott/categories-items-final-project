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
    origins = session.query(Origin).order_by('name').all()
    coffees = session.query(Coffee).order_by('name').all()
    return render_template('main.html', origins=origins, coffees=coffees)

@app.route('/add-origin', methods=['GET', 'POST'])
def addOrigin():
    if request.method == 'POST':
        new_origin = request.form['new-origin'].title()
        try:
            session.query(Origin).filter_by(name=new_origin).one()
            return redirect(url_for('showHomePage'))
        except:
            newOrigin = Origin(name=new_origin)
            session.add(newOrigin)
            session.commit()
            return redirect(url_for('showHomePage'))
    return render_template('add-origin.html')

@app.route('/show-origin/<int:origin_id>', methods=['GET', 'POST'])
def showOrigin(origin_id):
    origin = session.query(Origin).filter_by(id=origin_id).one()
    coffees = session.query(Coffee).filter_by(origin_id=origin_id
        ).order_by('name').all()
    if request.method == 'POST':
        pass
    return render_template('show-origin.html', origin=origin, coffees=coffees)

@app.route('/add-coffee-from/<int:origin_id>', methods=['GET', 'POST'])
def addCoffeeFrom(origin_id):
    origin = session.query(Origin).filter_by(id=origin_id).one()
    if request.method == 'POST':
        try:
            session.query(Coffee).filter_by(origin_id=origin_id,
                                            name=request.form['new-coffee']
                                            ).one()
            return redirect(url_for('showOrigin', origin_id=origin_id))
        except:
            newCoffee = Coffee(name=request.form['new-coffee'],
                                description=request.form['coffee-description'],
                                origin_id=origin_id)
            session.add(newCoffee)
            session.commit()
            return redirect(url_for('showOrigin', origin_id=origin_id))

    return render_template('add-coffee-from.html', origin=origin)

@app.route('/add-coffee', methods=['GET', 'POST'])
def addCoffee():
    origins = session.query(Origin).all()
    if request.method == 'POST':
        origin = session.query(Origin).filter_by(
            name=request.form['selected-origin']).one()
        newCoffee = Coffee(name=request.form['new-coffee'],
                            description=request.form['coffee-description'],
                            origin_id=origin.id)
        session.add(newCoffee)
        session.commit()
        return redirect(url_for('showHomePage'))
    return render_template('add-coffee.html', origins=origins)

@app.route('/show-coffee/<int:coffee_id>', methods=['GET'])
def showCoffee(coffee_id):
    coffee = session.query(Coffee).filter_by(id=coffee_id).one()
    origin = session.query(Origin).filter_by(id=coffee.origin_id).one()
    return render_template('show-coffee.html', coffee=coffee, origin=origin)



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
