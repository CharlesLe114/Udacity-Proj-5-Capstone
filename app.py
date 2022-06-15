from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Hello World, my name is Le Bao Toan \
#             This is the Capstone project</h1>'

@app.route("/")
def home():
    html = f"<h3>Hello World, my name is Le Bao Toan \
            This is the Capstone project</h3>"
    return html.format(format)

app.run(host='localhost', port=80)