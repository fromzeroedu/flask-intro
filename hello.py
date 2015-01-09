from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form.get('username'),
                        request.form.get('password')):
            return "Welcome back, %s" % request.form.get('username')
        else:
            error = "Incorrect username and password"
    return render_template('login.html', error=error)

def valid_login(username, password):
    if username == password:
        return True
    else:
        return False

if __name__ == '__main__':
    app.debug = True
    app.run()
