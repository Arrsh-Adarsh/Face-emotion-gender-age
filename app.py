from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')
#<link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">

if __name__ == '__main__':
    app.run(debug=True)
