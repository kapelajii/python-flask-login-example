from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return '<h1>This is main index page</h1>'