from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    i = 1
    return 'Hello World!'  + i

if __name__ == '__main__':
    app.debug = True
    app.run()
