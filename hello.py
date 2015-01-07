from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def show_url_for():
    # display the url for a function
    return url_for('show_user_profile', username='jorge')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

if __name__ == '__main__':
    app.debug = True
    app.run()
