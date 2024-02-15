from app.utils.database import db

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(100), nullable=False)
    habitat = db.Column(db.String(100), nullable=False)
    countries = db.Column(db.String(100), nullable=False)
