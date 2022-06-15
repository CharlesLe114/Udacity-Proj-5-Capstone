from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World, my name is Le Bao Toan \
            This is the Capstone project</h1>'

app.run(host='localhost', port=80)