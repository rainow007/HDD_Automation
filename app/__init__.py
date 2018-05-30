<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)
=======
# coding:utf-8
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


'''配置数据库'''
app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'hard to guess'
# 这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名jianshu,连接方式参考 \
# http://docs.sqlalchemy.org/en/latest/dialects/mysql.html

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:IamLGY847464505@localhost:3306/test_flask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:621067@localhost:3306/test_flask'
# 设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 实例化
db = SQLAlchemy(app)

UPLOAD_FOLDER = '../upload/dingdang_auto/TestCase'
basedir = os.path.abspath(os.path.dirname(__file__))
# basedir = '/home/svn/Taffy_Web-master/app'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(
    ['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF','py','yml'])

>>>>>>> the lastst version on 2018/05
from app import views, forms
