from flask import Flask
from flask import Blueprint

simple=Blueprint("simple",__name__)
@simple.route("/")
def index():
    return "hello world"

if __name__ == '__main__':
    app=Flask(__name__)
    app.register_blueprint(simple)
    app.run()

