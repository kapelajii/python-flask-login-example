
from decouple import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import UserMixin


from main import main as main_blueprint
from auth import auth as auth_blueprint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = config('SECRET_KEY')

db = SQLAlchemy(app)

db.init_app(app)

# Register blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    app.run(debug=config('DEBUG'), host= '0.0.0.0')