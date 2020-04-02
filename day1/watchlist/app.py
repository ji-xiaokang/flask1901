import os,sys
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy     #导入扩展类
import click
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.path.join(app.root_path,'data.db')      #linux
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(app.root_path,'data.db')     #windows
app.config['SQLALCHY_TRACK_MODIFCATIONS'] = False    # 关闭了对模型修改的监控
db = SQLAlchemy(app)    # 初始化扩展，传入程序实例app

# models
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

#views    
@app.route('/')
# @app.route('/index') 
# @app.route('/home')

def index():
    name = "中国"
    movies = [
        { "title" : "大赢家" , "year" : "2020" },
        { "title" : "叶问4" , "year" : "2020" },
        { "title" : "唐人街探案" , "year" : "2020" },
        { "title" : "囧妈" , "year" : "2020" },
        { "title" : "你麻痹" , "year" : "2020" },
    ]
    return render_template("index.html",name=name,movies=movies)


# 自定义命令
@app.cli.command()  # 装饰器，注册命令
@click.option('--drop',is_flag=True,help="删除后再创建")
def initdb(drop):
    if drop:
        db.drop_all()    
    db.create_all()
    click.echo("初始化数据库完成")