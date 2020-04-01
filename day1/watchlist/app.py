from flask import Flask
from flask import render_template
app = Flask(__name__)

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