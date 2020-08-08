from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        print(request.form['name'])
        data = 'Hello, ' + request.form['name']
        return render_template('home.html', data=data)
    else:
        data = 'Hello, World!'
    return data
