import os
from datetime import datetime

from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# def render_template(path, **data):
#     if not "debug" in data.keys():
#         data["debug"] = app.config["DEBUG"]
#
#     return flask.render_template(path, **data)


@app.route("/")
def hello():
    return jsonify({
        "name": "Hello World from Flask! 2",
        "count": 0,
        "created": datetime.utcnow(),
    })


@app.route("/index.html")
def hello_html():
    template = """
        <table>
            <tr>
                <th>name</th>
                <th>count</th>
                <th>created</th>
            </tr>
            <tr>
                <td>{{name}}</td>
                <td>{{count}}</td>
                <td>{{created}}</td>
            </tr>
        </table>
    """

    return render_template_string(
        template,
        name="Hello World from Flask! 2",
        count=0,
        created=datetime.utcnow()
    )


if __name__ == "__main__":
    port = int(os.environ.get('FLASK_PORT', 80))
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    app.run(host=host, debug=True, port=port)
