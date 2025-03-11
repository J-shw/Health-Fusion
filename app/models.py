from flask_sqlalchemy import SQLAlchemy
from app import db # Import the db instance from app.py

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Add other models here...