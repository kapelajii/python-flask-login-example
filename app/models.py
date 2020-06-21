from app import db

class user(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.string(100))
    name = db.Column(db.String(500))
