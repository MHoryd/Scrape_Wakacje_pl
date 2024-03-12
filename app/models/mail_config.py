from app.extensions import db

class mail_config(db.Model):
    __tablename__ = 'mail_config'
    id = db.Column(db.Integer, primary_key=True)
    notification_email = db.Column(db.String(100))
    notification_receivers_email = db.Column(db.String(100))
    notification_pass = db.Column(db.String(100))
    notification_smtp_server = db.Column(db.String(100))