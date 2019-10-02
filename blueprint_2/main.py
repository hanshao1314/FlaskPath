from flask import Flask
from bluePrint_1 import simple1
from bluePrint_2 import simple2

if __name__ == '__main__':
    app=Flask(__name__)
    app.register_blueprint(simple1)
    app.register_blueprint(simple2)
    app.run()
