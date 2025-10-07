from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, WorlDADA!'

@app.route('/movies', methods=["GET"])
def hello():
    return 'This is test page!! Can you see this?'

@app.route('/movies/exists', methods=["GET"])
def movie_exists():
    return 'This movie exists!! Can you see this?'

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)