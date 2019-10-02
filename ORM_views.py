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

#定义表
class Curriculum(models.Model):
    __tablename__="curriculum"
    id=models.Column(models.Integer,primary_key=True)
    c_id=models.Column(models.String(32))
    c_name=models.Column(models.String(32))
    c_time=models.Column(models.Date)

#创建表（同步）
models.create_all()

# ORM操作如下
import datetime
session=models.session()
#""" ——————增加——————"""
# 增加单条
# c1=Curriculum(c_id="0007",c_name="Djngo",c_time=datetime.datetime.now())
# session.add(c1)
# session.commit()

# 增加多条数据
# c1=Curriculum(c_id="0001",c_name="python",c_time=datetime.datetime.now())
# c2=Curriculum(c_id="0002",c_name="面向对象",c_time=datetime.datetime.now())
# c3=Curriculum(c_id="0003",c_name="html",c_time=datetime.datetime.now())
# c4=Curriculum(c_id="0004",c_name="mysql",c_time=datetime.datetime.now())
# c5=Curriculum(c_id="0005",c_name="linux",c_time=datetime.datetime.now())
# session.add_all([c1,c2,c3,c4,c5])
# session.commit()

"""——————查找——————"""
# all();查询所有
# all_c=Curriculum.query.all()
# for c in all_c:
#     print(c)

# filter_by():条件查找
# all_c=Curriculum.query.filter_by(c_id="0002")   #返回列表对象
# for c in all_c:
#     print(c.id,c.c_name)

#get()查询单条
# c=Curriculum.query.get(1)
# print(c.id,c.c_name)

# c=Curriculum.query.first()  #查找第一个数据
# print(c.id,c.c_name)

# 排序
# all_c=Curriculum.query.order_by("id")   #正序
# for c in all_c:
#     print(c.id,c.c_name)

# all_c=Curriculum.query.order_by(models.desc("id"))   #倒序
# for c in all_c:
#     print(c.id,c.c_name)

# :limit()分页查询
# all_c=Curriculum.query.offset(0).limit(2).all()
    # offset 偏移，在这里指的是查询的起始位置
    # limit 具体查询的数量
    # select * from curriculum limit 0,2 从0索引开始，查询两条
# for c in all_c:
#     print(c.id,c.c_name)

"""——————修改——————"""
c=Curriculum.query.get(4)
c.c_name="Mqsql"
session.add(c)
session.commit()




"""——————删除——————"""
# b1=Curriculum.query.get(5)
# print(b1)
# models.session.delete(b1)
# session.commit()

c=Curriculum.query.get(5)
print(c)
session.delete(c)
session.commit()