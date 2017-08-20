#!/usr/bin/python
# Author: Scott Iwako
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
from flask import url_for
from flask import flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Coffee, Origin, User
# client secret
from flask import session as login_session
import random
import string
# oath
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///coffeewithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "The Coffee App"

# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        dump = json.dumps('<p>Current user is already connected.</p>')
        response = make_response(dump, 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # See if a user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id


    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

def getUsersName(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user.name


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
        # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    print result

    if result['status'] == '200':
        # Reset the user's sesson.
        for key in login_session.keys():
            del login_session[key]

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return redirect(url_for('showHomePage'))
    else:
        # For whatever reason, the given token was invalid.
        for key in login_session.keys():
            del login_session[key]
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return redirect(url_for('showHomePage'))


# Shows the main page
@app.route('/')
@app.route('/home')
def showHomePage():
    origins = session.query(Origin).order_by('name').all()
    coffees = session.query(Coffee).order_by('name').all()

    try:
        creator = getUserInfo(login_session['user_id'])
        return render_template('main.html',
                                origins=origins,
                                coffees=coffees,
                                creator=creator)
    except:
        return render_template('main-public.html',
                                origins=origins,
                                coffees=coffees)


# adds origin
@app.route('/add-origin', methods=['GET', 'POST'])
def addOrigin():
    if request.method == 'POST':
        new_origin = request.form['new-origin'].title()
        try:
            session.query(Origin).filter_by(name=new_origin).one()
            return redirect(url_for('showHomePage'))
        except:
            newOrigin = Origin(name=new_origin,
                               user_id=login_session['user_id'])
            session.add(newOrigin)
            session.commit()
            return redirect(url_for('showHomePage'))
    try:
        creator = getUserInfo(login_session['user_id'])
        return render_template('add-origin.html', creator=creator)
    except:
        return """<script>
                  alert('Please log in to access this feature');
                  window.location.href="/home";
                  </script>"""


# show coffes from a particular region
@app.route('/show-coffees-from/<int:origin_id>', methods=['GET', 'POST'])
def showCoffeeFrom(origin_id):
    origin = session.query(Origin).filter_by(id=origin_id).one()
    coffees_query = session.query(Coffee).filter_by(origin_id=origin_id)
    coffees = coffees_query.order_by('name').all()
    try:
        creator = getUserInfo(login_session['user_id'])
        return render_template('show-origin.html',
                               origin=origin,
                               coffees=coffees,
                               creator=creator,
                               getUsersName=getUsersName)
    except:
        return render_template('show-origin-public.html',
                               origin=origin,
                               coffees=coffees,
                               getUsersName=getUsersName)


# adds coffee from a fixed origin
@app.route('/add-coffee-from/<int:origin_id>', methods=['GET', 'POST'])
def addCoffeeFrom(origin_id):
    origin = session.query(Origin).filter_by(id=origin_id).one()
    if request.method == 'POST':
        try:
            session.query(Coffee).filter_by(origin_id=origin_id,
                                            name=request.form['new-coffee']
                                            ).one()
            return redirect(url_for('showCoffeeFrom', origin_id=origin_id))
        except:
            newCoffee = Coffee(name=request.form['new-coffee'],
                               description=request.form['coffee-description'],
                               origin_id=origin_id,
                               user_id=login_session['user_id'])
            session.add(newCoffee)
            session.commit()
            return redirect(url_for('showCoffeeFrom', origin_id=origin_id))

    try:
        creator = getUserInfo(login_session['user_id'])
        return render_template('add-coffee-from.html',
                               origin=origin,
                               creator=creator)
    except:
        return """<script>
                  alert('Please log in to access this feature');
                  window.location.href="/home";
                  </script>"""

# adds a coffee from a user selected origin
@app.route('/add-coffee', methods=['GET', 'POST'])
def addCoffee():
    origins = session.query(Origin).order_by('name').all()
    if request.method == 'POST':
        origin = session.query(Origin).filter_by(
            name=request.form['selected-origin']).one()
        newCoffee = Coffee(name=request.form['new-coffee'],
                           description=request.form['coffee-description'],
                           origin_id=origin.id,
                           user_id=login_session['user_id'])
        session.add(newCoffee)
        session.commit()
        return redirect(url_for('showHomePage'))
    try:
        creator = getUserInfo(login_session['user_id'])
        return render_template('add-coffee.html',
                               origins=origins,
                               creator=creator)
    except:
        return """<script>
                  alert('Please log in to access this feature');
                  window.location.href="/home";
                  </script>"""


# shows a coffee
@app.route('/show-coffee/<int:coffee_id>', methods=['GET'])
def showCoffee(coffee_id):
    coffee = session.query(Coffee).filter_by(id=coffee_id).one()
    origin = session.query(Origin).filter_by(id=coffee.origin_id).one()
    try:
        creator = getUserInfo(login_session['user_id'])
        return render_template('show-coffee.html',
                               coffee=coffee,
                               origin=origin,
                               creator=creator,
                               getUsersName=getUsersName)
    except:
        return render_template('show-coffee-public.html',
                               coffee=coffee,
                               origin=origin,
                               getUsersName=getUsersName)


# shows all coffee from an origin
@app.route('/delete-coffee-from-list/<int:coffee_id>', methods=['GET', 'POST'])
def deleteCoffee(coffee_id):
    coffee = session.query(Coffee).filter_by(id=coffee_id).one()
    if request.method == 'POST':
        session.delete(coffee)
        session.commit()
        return redirect(url_for('showCoffeeFrom', origin_id=coffee.origin_id))

    try:
        creator = getUserInfo(login_session['user_id'])
        is_op = coffee.user_id == login_session['user_id']
        if is_op:
            return render_template('delete-coffee-from-list.html',
                               coffee=coffee,
                               creator=creator)
        else:
            return """<script>
                      alert('You are not authorized to delete this post.');
                      window.location.href="/home";
                      </script>
                      """
    except:
        return """<script>
                  alert('Please log in to access this feature');
                  window.location.href="/home";
                  </script>"""


# deletes a coffee
@app.route('/delete-coffee/<int:coffee_id>', methods=['GET', 'POST'])
def deleteCoffeeToHome(coffee_id):
    coffee = session.query(Coffee).filter_by(id=coffee_id).one()
    if request.method == 'POST':
        session.delete(coffee)
        session.commit()
        return redirect(url_for('showHomePage'))

    try:
        creator = getUserInfo(login_session['user_id'])
        is_op = coffee.user_id == login_session['user_id']
        if is_op:
            return render_template('delete-coffee.html',
                                   coffee=coffee,
                                   creator=creator)
        else:
            return """<script>
                      alert('You are not authorized to delete this post.');
                      window.location.href="/home";
                      </script>
                      """
    except:
        return """<script>
                  alert('Please log in to access this feature');
                  window.location.href="/home";
                  </script>"""


# edit coffee
@app.route('/edit-coffee/<int:coffee_id>', methods=['GET', 'POST'])
def editCoffee(coffee_id):
    coffee = session.query(Coffee).filter_by(id=coffee_id).one()
    origin = session.query(Origin).filter_by(id=coffee.origin_id).one()
    if request.method == 'POST':
        new_name = request.form['edit-coffee']
        new_descript = request.form['new-coffee-description']
        if new_name:
            coffee.name = new_name
        if new_descript:
            coffee.description = new_descript
        return redirect(url_for('showCoffeeFrom', origin_id=origin.id))

    try:
        creator = getUserInfo(login_session['user_id'])
        is_op = coffee.user_id == login_session['user_id']
        if is_op:
            return render_template('edit-coffee-redirect-to-list.html',
                                   coffee=coffee,
                                   origin=origin)
        else:
            return """<script>
                      alert('You are not authorized to edit this post.');
                      window.location.href="/home";
                      </script>
                      """
    except:
        return """<script>
                  alert('Please log in to access this feature');
                  window.location.href="/home";
                  </script>"""

# edit a coffee from a page dedicated to that coffee
@app.route('/edit-single-coffee/<int:coffee_id>', methods=['GET', 'POST'])
def editSingleCoffee(coffee_id):
    coffee = session.query(Coffee).filter_by(id=coffee_id).one()
    origin = session.query(Origin).filter_by(id=coffee.origin_id).one()
    if request.method == 'POST':
        coffee.name = request.form['edit-coffee']
        session.commit()
        return redirect(url_for('showCoffee', coffee_id=coffee.id))

    try:
        creator = getUserInfo(login_session['user_id'])
        is_op = coffee.user_id == login_session['user_id']
        if is_op:
            return render_template('edit-coffee.html',
                                   coffee=coffee,
                                   origin=origin,
                                   creator=creator)
        else:
            return """<script>
                      alert('You are not authorized to edit this post.');
                      window.location.href="/home";
                      </script>
                      """
    except:
        return """<script>
                  alert('Please log in to access this feature');
                  window.location.href="/home";
                  </script>"""



# delete an entire origin and all coffees from that origin
@app.route('/delete-origin/<int:origin_id>', methods=['GET', 'POST'])
def deleteOrigin(origin_id):
    origin = session.query(Origin).filter_by(id=origin_id).one()
    coffees = session.query(Coffee).filter_by(origin_id=origin_id).all()
    if request.method == 'POST':
        session.delete(origin)
        for coffee in coffees:
            session.delete(coffee)
        session.commit()
        return redirect(url_for('showHomePage'))

    try:
        creator = getUserInfo(login_session['user_id'])
        is_op = origin.user_id == login_session['user_id']
        if is_op:
            return render_template('delete-origin.html',
                                   origin=origin,
                                   coffees=coffees,
                                   creator=creator)
        else:
            return """<script>
                      alert('You are not authorized to delete this origin.');
                      window.location.href="/home";
                      </script>
                      """
    except:
        return """<script>
                  alert('Please log in to access this feature');
                  window.location.href="/home";
                  </script>"""

# edit origin name
@app.route('/edit-origin-name/<int:origin_id>', methods=['GET', 'POST'])
def editOriginName(origin_id):
    origin = session.query(Origin).filter_by(id=origin_id).one()
    if request.method == 'POST':
        origin.name = request.form['origin-edit']
        session.commit()
        return redirect(url_for('showCoffeeFrom', origin_id=origin.id))
    try:
        creator = getUserInfo(login_session['user_id'])
        is_op = origin.user_id == login_session['user_id']
        if is_op:
            return render_template('edit-origin.html',
                                   origin=origin,
                                   creator=creator)
        else:
            return """<script>
                      alert('You are not authorized to edit this post.');
                      window.location.href="/home";
                      </script>
                      """
    except:
        return """<script>
                  alert('Please log in to access this feature');
                  window.location.href="/home";
                  </script>"""


# JSONIFY
# JSON for all Coffees
@app.route('/home/coffees/JSON', methods=['GET'])
def coffeesJSON():
    coffees = session.query(Coffee).all()
    return jsonify(coffees=[c.serialize for c in coffees])


# JSON for a Coffee
@app.route('/show-coffee/<int:coffee_id>/JSON', methods=['GET'])
def coffeeJSON(coffee_id):
    coffee = session.query(Coffee).filter_by(id=coffee_id).one()
    return jsonify(coffee=coffee.serialize)


# JSON for all Origins
@app.route('/home/origins/JSON', methods=['GET'])
def originsJSON():
    origins = session.query(Origin).all()
    return jsonify(origins=[o.serialize for o in origins])


# JSON for all Coffees for an Origin
@app.route('/show-coffees-from/<int:origin_id>/JSON', methods=['GET'])
def coffeesFromOriginJSON(origin_id):
    coffees = session.query(Coffee).filter_by(origin_id=origin_id)
    return jsonify(coffees=[c.serialize for c in coffees])


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
