# @author HHN
# @Copyright https://haojie.org
#导入Flask库
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from admin import admin_blueprint

#创建app 实例
app = Flask(__name__)
app.debug = True #打开调试
app.secret_key = 'haojieorg' #增加安全码

#配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


@app.route('/')
def index():
    return '欢迎使用Flask'

@app.route('/login/')
def login():
    return render_template('login.html')

app.register_blueprint(admin_blueprint,url_prefix='/admin')

if __name__ == '__main__':
    app.run()