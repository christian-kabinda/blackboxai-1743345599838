from datetime import datetime
from app import db

class JobApplication(db.Model):
    __tablename__ = 'job_application'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    application_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    status = db.Column(db.String(50), default='Applied')
    source = db.Column(db.String(50))  # LinkedIn, Indeed, etc.
    job_description = db.Column(db.Text)
    next_followup = db.Column(db.DateTime)
    notes = db.Column(db.Text)

    def __repr__(self):
        return f'<JobApplication {self.position} at {self.company}>'