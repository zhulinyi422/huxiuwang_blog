import re
import os
from flask import Blueprint,render_template,request,redirect,url_for,jsonify,session
from APP.models import User
from APP.models import db
from utils.setting import UPLOAD_DIR
from utils.functions import is_login

user_blueprint = Blueprint('user',__name__)

@user_blueprint.route('/create_db/')
def create_db():
    db.create_all()
    return '创建成功'

@user_blueprint.route('/register/',methods=['GET'])
def register_g():
    return render_template('register.html')

@user_blueprint.route('/register/',methods=['POST'])
def register_p():
    username = request.form.get('username')
    pwd1 = request.form.get('pwd1')
    pwd2 = request.form.get('pwd2')
    img_file = request.files.get('avatar')
    company = request.form.get('company')
    weibo = request.form.get('weibo')
    job = request.form.get('job')
    we_chat = request.form.get('we_chat')
    e_mail = request.form.get('e_mail')
    we_public = request.form.get('we_public')
    info = request.form.get('info')
    if not all([username,pwd1,pwd2]):
        return '请填写必填字段'
    if pwd1 != pwd2 :
        return '两次输入的密码不符合'
    user = User.query.filter_by(name=username).first()
    if user:
        return '该用户名已经存在'
    else:
        user = User()
        user.name = username
        user.password = pwd1
        image_path = os.path.join(UPLOAD_DIR,img_file.filename)
        img_file.save(image_path)
        user.avatar = os.path.join('upload',img_file.filename)
        user.company = company
        user.weibo = weibo
        user.job = job
        user.we_chat = we_chat
        user.e_mail = e_mail
        user.info = info
        try:
            user.add_update()
        except Exception as e:
            db.session.rollback()
            return '创建用户失败'
        return redirect(url_for('user.login_g'))



@user_blueprint.route('/login/',methods=['GET'])
def login_g():
    return render_template('login.html')

@user_blueprint.route('/login/',methods=['POST'])
def login_p():
    username = request.form.get('username')
    password = request.form.get('password')
    if not all([username,password]):
        return '请输入完整参数'
    user = User.query.filter_by(name=username).first()
    if user:
        session['user_id'] = user.id
        return redirect(url_for('blog.index'))
    else:
        return '该用户不存在'

@user_blueprint.route('/logout/',methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('user.login_g'))


# 个人信息页面
@user_blueprint.route('/member_g/',methods=['GET'])
@is_login
def member_g():
    user = User.query.get(session['user_id'])
    return jsonify(user_info=user.to_dict(),username=user.name)


@user_blueprint.route('/u_article/',methods=['GET'])
def u_article():
    user = User.query.get(session['user_id'])
    articles = [article.to_dict() for article in user.articles]
    return jsonify(articles=articles)