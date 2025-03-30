from datetime import datetime
from app import db

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sender = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200))
    received_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    category = db.Column(db.String(50))  # Job, Networking, Other
    body = db.Column(db.Text)
    is_responded = db.Column(db.Boolean, default=False)
    response_draft = db.Column(db.Text)
    importance = db.Column(db.Integer, default=1)  # 1-5 scale

    def __repr__(self):
        return f'<Email from {self.sender} - {self.subject}>'