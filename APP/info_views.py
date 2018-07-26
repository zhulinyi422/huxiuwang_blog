import random
from flask import Blueprint,render_template,request,redirect,url_for,jsonify,session
from APP.models import Article,User,Comment

info_blueprint = Blueprint('info',__name__)

@info_blueprint.route('/article_info/',methods=['GET'])
def article_info():
    try:
        user = User.query.get(session['user_id'])
        return render_template('article.html',user=user)
    except:
        return render_template('article.html')

@info_blueprint.route('/article_info/<int:id>/',methods=['GET'])
def article_content(id):
    article = Article.query.get(id)
    comment_list = article.comments
    comments = [comment.to_dict() for comment in comment_list]
    type = article.type.type_name
    type_info = article.type.id
    articles_test = Article.query.filter_by(type_id=type_info)
    articles = list(articles_test)
    random.shuffle(articles)
    articless = articles[0:4]
    article_list = [i.to_dict() for i in articless]
    auth_name = article.user.name
    auth_img = article.user.avatar
    return jsonify(article=article.to_dict(),data={'type':type,'auth_name':auth_name,'auth_img':auth_img,'article_list':article_list},comments=comments)


@info_blueprint.route('/comment/',methods=['POST'])
def comment():
    user = User.query.get(session['user_id'])
    comment_info = Comment()
    a_id = request.form.get('id')
    article = Article.query.get(a_id)
    comment_info.content = request.form.get('info')
    comment_info.user_id = user.id
    comment_info.article_id = request.form.get('id')
    comment_info.add_update()
    comment_list = article.comments
    comments = [comment.to_dict() for comment in comment_list]
    return jsonify(comments=comments)

