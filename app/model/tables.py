from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(60))
    password = db.Column(db.String(50))
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    
    def __init__(self, username, email, password, name):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
