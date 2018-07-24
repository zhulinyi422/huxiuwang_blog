import random
from flask import Blueprint,render_template,session,jsonify,redirect,url_for,request
from APP.models import User,Type,Article
from utils.functions import is_login

house_blueprint = Blueprint('blog',__name__)

# 首页
@house_blueprint.route('/')
def index():
    try:
        user = User.query.get(session['user_id'])
        articles = user.articles[0:2]
        b_article = user.articles[-1]
        return render_template('index.html',articles=articles,b_article=b_article)
    except:
        user = User.query.get(3)
        articles = user.articles[0:2]
        b_article = user.articles[-1]
        return render_template('index.html',articles=articles,b_article=b_article)

# 首页的Ajax
@house_blueprint.route('/index/')
def index_g():
    try:
        user = User.query.get(session['user_id'])
    except:
        return jsonify(code=1001)
    return jsonify(code=200,username=user.name)

# 首页的所有文章信息
@house_blueprint.route('/index_article/')
def index_article():
    article_list = Article.query.all()
    index_articles = random.sample(article_list,30)
    articles = [article.to_dict() for article in index_articles]
    return jsonify(articles=articles)


#  咨询栏的ajax
@house_blueprint.route('/info_list/')
def info_list():
    types = Type.query.all()
    type_lists = [type.to_dict() for type in types]
    return jsonify(type_lists=type_lists)


# 活动页
@house_blueprint.route('/active/')
def active():
    return render_template('active.html')



@house_blueprint.route('/member/',methods=['GET'])
@is_login
def member():
    return render_template('member.html')

@house_blueprint.route('/choice/',methods=['GET'])
def choice():
    return render_template('choice.html')

@house_blueprint.route('/choice/<int:id>/',methods=['GET'])
def choice_info(id):
    type = Type.query.get(id)
    articles = type.articles
    article_list = [article.to_dict() for article in articles]
    types = Type.query.all()
    type_list = [type1.to_dict() for type1 in types]
    list1 = [0,1,2,3,4,5,6,7,8,9,10,11]
    random.shuffle(list1)
    list_tem = list1[0:6]
    pindao_list = [type_list[list_tem[0]],type_list[list_tem[1]],type_list[list_tem[2]],
                   type_list[list_tem[3]],type_list[list_tem[4]],type_list[list_tem[5]]]
    return jsonify(article_list=article_list,typename=type.type_name,pindao_list=pindao_list)

@house_blueprint.route('/choice_hot/<int:id>/',methods=['GET'])
def choice_hot(id):
    type = Type.query.get(id)
    article_lists = type.articles
    articles = [article.to_dict() for article in article_lists]
    list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    random.shuffle(list1)
    list_tem = list1[0:10]
    hot_content = [articles[list_tem[0]],articles[list_tem[1]],articles[list_tem[2]],
                   articles[list_tem[3]],articles[list_tem[4]],articles[list_tem[5]],
                   articles[list_tem[6]],articles[list_tem[7]],articles[list_tem[8]],
                   articles[list_tem[9]]]
    return jsonify(hot_content=hot_content)

# 搜索栏
@house_blueprint.route('/search_info/',methods=['GET'])
def search_info():
    info = request.args.get('info')
    search_val = '%{}%'.format(info)
    articles = Article.query.filter(Article.title.ilike(search_val)).all()
    article_list = [article.to_dict() for article in articles]
    list1 = []
    for _ in article_list:
        _['content'] = _['content'][:120]
        list1.append(_)
    return jsonify(articles=list1)


@house_blueprint.route('/search/',methods=['GET'])
def search():
    return render_template('search.html')