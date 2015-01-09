from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
            return "User %s logged in" % request.form['username']
    return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
