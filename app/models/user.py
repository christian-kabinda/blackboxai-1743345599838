from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    jobs_applied = db.relationship('JobApplication', backref='applicant', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.email}>'