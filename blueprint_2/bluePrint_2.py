from flask import Blueprint

simple2=Blueprint("simple2",__name__)
@simple2.route("/2")
def index():
    return "hello world 2"


