import random
from flask import Blueprint,render_template,request,redirect,url_for,jsonify,session
from APP.models import Article,User

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
    type = article.type.type_name
    type_info = article.type.id
    articles_test = Article.query.filter_by(type_id=type_info)
    articles = list(articles_test)
    random.shuffle(articles)
    articless = articles[0:4]
    article_list = [i.to_dict() for i in articless]
    auth_name = article.user.name
    auth_img = article.user.avatar
    return jsonify(article=article.to_dict(),data={'type':type,'auth_name':auth_name,'auth_img':auth_img,'article_list':article_list})

