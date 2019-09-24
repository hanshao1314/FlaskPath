"""
flask当中，可以直接创建应用，进行开发，而django是现有项目，再创建应用，但是在工作当中flask
也会遇到多应用问题，也需要有项目框架，只不过这个框架被称为 蓝图（blueprint）
"""
from flask import Flask
# 创建一个app应用
app=Flask(__name__)
@app.route("/index/")  #创建路由
def index():  #：创建视图
    return "hello world "

@app.route("/list/")
def list():
    return "hello list"

@app.route("/content/<username>/<int:age>/")
def content(username,age):
    return "hello,I'm %s ,I'm %s years old"%(username,age)

import datetime,time
# @app.route("/birthday/<month>/<int:day>/")
@app.route("/birthday/")
def brithday():
    now = time.time()
    bir = time.mktime(time.struct_time((2019, 2, 18, 0, 0, 0, 0, 0, 0)))
    day = (now - bir) / 60 / 60 / 24
    # return r"生日是%s月%日，是当年的第%s天"%(str(day))
    return r"当前生日是当年的第%s天"%(str(day))

# @app.route("/birthday/<month>/<int:day>/")
@app.route("/bdy/month/day/")
def brithday(month,day):
    now_time=datetime
    now = time.time()
    bir = time.mktime(time.struct_time((2019, 2, 18, 0, 0, 0, 0, 0, 0)))
    day = (now - bir) / 60 / 60 / 24
    # return r"生日是%s月%日，是当年的第%s天"%(str(day))
    return r"当前生日是当年的第%s天"%(str(day))

if __name__=="__main__":
    # app.run()  #启动应用，此时默认端口是5000
    app.run(host="127.0.0.1",port=8000,debug=True)   #启动应用，修改之后端口是8000


