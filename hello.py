from flask import Flask, request, render_template, redirect, url_for, flash, session
import logging
from logging.handlers import RotatingFileHandler
from flaskext.mysql import MySQL
import os

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form.get('username'),
                        request.form.get('password')):
            flash("Succesfully logged in")
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = "Incorrect username and password"
            app.logger.warning('Incorrect username passwword for user (%s)',
                                request.form.get('username'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))

def valid_login(username, password):
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from user where username='%s' and password='%s'" %
                    (username, password))
    data = cursor.fetchone()
    if data:
        return True
    else:
        return False

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'SuperSecretKey'

    # logging
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    #mysql
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'fromzero'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'test'
    app.config['MYSQL_DATABASE_DB'] = 'my_flask_app'
    app.config['MYSQL_DATABASE_HOST'] = os.getenv('IP', '0.0.0.0')
    mysql.init_app(app)

    # run
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 5000)))
