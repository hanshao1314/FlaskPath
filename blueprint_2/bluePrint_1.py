from flask import Blueprint

simple1=Blueprint("simple1",__name__)
@simple1.route("/1")
def index():
    return "hello world 1"

