from app.extensions import db

class Destinations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(60),nullable=False, unique=True)
    country_label = db.Column(db.String(60),nullable=False, unique=True)