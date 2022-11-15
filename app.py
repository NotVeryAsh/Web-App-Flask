from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/blog/<string:post_title>")
def view_blog_post(post_title):
    return f"<h2>You are viewing Blog Post: '{escape(post_title)}'</h2>"


@app.route("/order/<int:record_id>")
def view_record(record_id):
    return f"Found record with id '{escape(record_id)}"


@app.route("/user/<uuid:user_id>")
def view_user(user_id):
    return f"Found user with id '{escape(user_id)}"


@app.route("/float/<float:number>")
def view_float(number):
    return f"This float is '{escape(number)}"


@app.route("/breadcrumb/<path:slug>")
def breadcrumb(slug):
    return f"Resources found at path '{escape(slug)}"


@app.route("/<name>")
def hello(name):
    return f"The page '{escape(name)}' could not be found"
