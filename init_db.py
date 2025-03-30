from app import create_app, db
from app.models.job import JobApplication
from app.models.user import User

app = create_app()
with app.app_context():
    # Create tables without enforcing foreign keys
    db.engine.execute('PRAGMA foreign_keys=OFF')
    
    # Create all tables
    db.create_all()
    
    # Re-enable foreign key constraints
    db.engine.execute('PRAGMA foreign_keys=ON')
    
    print("Database tables created successfully")