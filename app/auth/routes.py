from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login')
def login():
    return '<h1>This is auth login page</h1>'