from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello, World!'

@app.route('/foo/')

def foo():
    return 'The foo page'

@app.route('/bar')

def bar():
    return 'The bar page'

@app.route('/hello/<name>')
def hello(name):
    return f"Hello {name}!"