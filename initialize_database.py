from app import create_app, db
from app.models.job import JobApplication
from app.models.user import User

app = create_app()
with app.app_context():
    # Create tables without enforcing foreign keys
    with db.engine.begin() as connection:
        if db.engine.name == 'sqlite':
            connection.execute('PRAGMA foreign_keys=OFF')
        
        db.create_all()
        
        if db.engine.name == 'sqlite':
            connection.execute('PRAGMA foreign_keys=ON')
    
    print("Database tables created successfully")