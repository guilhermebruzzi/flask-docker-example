import os
from datetime import datetime

from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

# def render_template(path, **data):
#     if not "debug" in data.keys():
#         data["debug"] = app.config["DEBUG"]
#
#     return flask.render_template(path, **data)

count = 0
created = datetime.utcnow()
updated = datetime.utcnow()


def update_counter(new_count):
    global count, updated
    count = new_count
    updated = datetime.utcnow()


def inc_counter():
    update_counter(count + 1)


def del_counter():
    update_counter(0)


def get_context():
    return {
        "name": "My counter",
        "count": count,
        "created": created,
        "updated": updated
    }


@app.route("/", methods=['GET', 'POST', 'DELETE'])
def counter():
    if request.method == 'POST':
        inc_counter()
    if request.method == 'DELETE':
        del_counter()
    return jsonify(get_context())


@app.route("/index.html", methods=['GET'])
def counter_html():
    template = """
        <style>
            table {
                width: 100%;
            }
            table td, table th {
                border: 1px solid;
                text-align: center;
                font-size: 30px;
            }
        </style>
        <table>
            <tr>
                <th>name</th>
                <th>count</th>
                <th>created</th>
                <th>updated</th>
            </tr>
            <tr>
                <td>{{name}}</td>
                <td>{{count}}</td>
                <td>{{created}}</td>
                <td>{{updated}}</td>
            </tr>
        </table>
    """

    return render_template_string(
        template, **get_context()
    )


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    app.run(host=host, debug=True, port=port)
