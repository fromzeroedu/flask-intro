from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    if request.values:
        return "username is " + request.values['username']
    else:
        return '<form method="get" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'

if __name__ == '__main__':
    app.debug = True
    app.run()
