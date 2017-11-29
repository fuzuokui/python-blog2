# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


print "加载配置文件内容"
app = Flask(__name__)
app.config.from_object('blog2.setting')#第一种配置参数的方法
# app.config.from_envvar('FLASKR_SETTINGS')#第二种配置参数的方法，通过环境变量

#创建数据库对象
db = SQLAlchemy(app)

print "只有在app对象之后声明，用于导入model否则无法创建表"
from blog2.model import User, Category

print "只有在app对象之后声明，用于导入view模块"
from blog2.controller import blog_message