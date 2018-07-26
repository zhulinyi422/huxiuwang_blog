from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(object):


    def add_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class User(BaseModel,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True) # 用户id
    name = db.Column(db.String(256))  # 用户名
    password = db.Column(db.String(256),unique=True)  #用户密码
    avatar = db.Column(db.String(256))   # 头像
    company = db.Column(db.String(256))   #公司
    weibo = db.Column(db.String(256))   # 微博
    job = db.Column(db.String(256))   # 工作
    we_chat = db.Column(db.String(256))   # 微信
    e_mail = db.Column(db.String(256))   # 邮箱
    info = db.Column(db.String(256))   # 用户简介
    articles = db.relationship('Article',backref='user')
    comments = db.relationship('Comment', backref='user')

    def to_dict(self):
        return {
            'name':self.name,
            'password':self.password,
            'avatar':self.avatar,
            'company':self.company,
            'weibo':self.weibo,
            'job':self.job,
            'we_chat':self.we_chat,
            'e_mail':self.e_mail,
            'info':self.info
        }

class Type(BaseModel,db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    type_name = db.Column(db.String(512))
    articles = db.relationship('Article',backref='type')
    def to_dict(self):
        return {
            'id':self.id,
            'type_name':self.type_name
        }


class Article(BaseModel,db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(512))
    content = db.Column(db.String(512))
    img = db.Column(db.String(512))
    type_id = db.Column(db.Integer,db.ForeignKey('type.id'),nullable=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=True)
    comments = db.relationship('Comment',backref='article')
    def to_dict(self):
        return {
            'id':self.id,
            'title':self.title,
            'content':self.content,
            'img':self.img,
            'type':self.type.type_name,
            'type_id':self.type_id,
            'auth':self.user.name
        }

class Comment(BaseModel,db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(512))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=True)
    article_id = db.Column(db.Integer,db.ForeignKey('article.id'),nullable=True)

    def to_dict(self):
        return {
            'id':self.id,
            'content':self.content,
            'user_avatar':self.user.avatar,
            'user_name':self.user.name
        }

