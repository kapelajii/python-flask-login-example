from decouple import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Build flask app
app=Flask(__name__)
# Database for app
db = SQLAlchemy(app)

# Settings 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
app.config['SECRET_KEY'] = config('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init login handling
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# login manager and user loader

# database user class import
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 

# Register blueprints
from main import main as main_blueprint
from auth import auth as auth_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')