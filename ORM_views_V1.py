import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app=Flask(__name__)  #实例化app

# 配置参数
BASE_DIR=os.path.abspath(os.path.dirname(__file__))

# app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(BASE_DIR,"ORM.sqlite")   #数据库地址 sqllite
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:111111@localhost/demo3"   #数据库地址 sqllite
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]=True   #请求结束后自动提交
app.config["SQLALCHEMY_RTACK_MODIFICATIONS"]=True   #flask1版本之后，添加的选项，目的是跟踪修改

#orm关联应用
models=SQLAlchemy(app)


# #创建表（同步）
# models.create_all()

class BaseModel(models.Model):
    __abstract__=True  #声明当前类是抽象类，被继承调用不创建
    id=models.Column(models.Integer,primary_key = True,autoincrement=True)
    def save(self):
        db=models.session()
        db.add(self)
        db.commit()
    def delete(self):
        db=models.session()
        db.delete(self)
        db.commit()

#定义表
class Curriculum(BaseModel):
    __tablename__="curriculum"
    id=models.Column(models.Integer,primary_key=True)
    c_id=models.Column(models.String(32))
    c_name=models.Column(models.String(32))
    c_time=models.Column(models.Date)

c=Curriculum.query.get(3)
print(c.c_name)
c.delete()