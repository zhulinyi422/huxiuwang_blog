from functools import wraps
from flask import session,redirect,url_for

'''
装饰器,验证是否登录
'''

def is_login(func):
    @wraps(func)
    def check_login():
        user_session = session.get('user_id')
        #验证成功
        if user_session:
            return func()
        #验证失败
        else:
            return redirect(url_for('user.login_g'))

    return check_login


