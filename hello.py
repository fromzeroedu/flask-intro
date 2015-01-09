from flask import Flask, request, render_template, redirect, url_for, flash
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form.get('username'),
                        request.form.get('password')):
            flash("Succesfully logged in")
            return redirect(url_for('welcome', username=request.form.get('username')))
        else:
            error = "Incorrect username and password"
    return render_template('login.html', error=error)

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

def valid_login(username, password):
    if username == password:
        return True
    else:
        return False

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'SuperSecretKey'
    app.run()
