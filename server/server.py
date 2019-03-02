from flask import Flask
app = Flask(__name__)


def add(datapoint, classifier):
    return 0


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/good", methods=('POST'))
def train():
    if request.method == 'POST':
        title = request.form['title'] 


