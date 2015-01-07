from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        return 'logged in'
    else:
        return '<form method="get" action="/login"><input type="text" /><p><button type="submit">Submit</button></form>'

if __name__ == '__main__':
    app.debug = True
    app.run()
