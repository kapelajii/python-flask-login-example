""" 
from decouple import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


from main import main as main_blueprint
from auth import auth as auth_blueprint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
app.config['SECRET_KEY'] = config('SECRET_KEY')

db = SQLAlchemy(app)

from models import User

# login handling
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader()
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)




if __name__ == '__main__':
    app.run(debug=config('DEBUG'), host= '0.0.0.0') """