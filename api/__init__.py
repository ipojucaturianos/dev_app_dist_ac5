from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///controle_acesso.db"
db = SQLAlchemy(app)

from app.controller import default
