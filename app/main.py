import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from Flask! :D"


if __name__ == "__main__":
    port = int(os.environ.get('FLASK_PORT', 80))
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    app.run(host=host, debug=True, port=port)
