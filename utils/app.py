import os

from flask import Flask
import redis
from APP.blog_views import house_blueprint
from flask_session import Session
from APP.user_views import user_blueprint
from APP.info_views import info_blueprint
from utils.setting import BASE_DIR
from APP.models import db



def create_app():
    static_dir = os.path.join(BASE_DIR,'static')
    templates_dir = os.path.join(BASE_DIR,'templates')
    app = Flask(__name__,static_folder=static_dir,template_folder=templates_dir)
    app.register_blueprint(blueprint=house_blueprint,url_prefix='/blog')
    app.register_blueprint(blueprint=user_blueprint,url_prefix='/user')
    app.register_blueprint(blueprint=info_blueprint,url_prefix='/info')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zly1995422@localhost:3306/blog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)
    app.config['SESSION_KEY_PREFIX'] = 'flask'
    db.init_app(app=app)
    Session(app=app)
    return app