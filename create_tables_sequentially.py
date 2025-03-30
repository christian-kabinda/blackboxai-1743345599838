from app import create_app, db
from sqlalchemy import text

def create_tables():
    app = create_app()
    with app.app_context():
        try:
            # Create User table first
            with db.engine.connect() as conn:
                conn.execute(text('''
                    CREATE TABLE IF NOT EXISTS user (
                        id INTEGER PRIMARY KEY,
                        email VARCHAR(120) UNIQUE NOT NULL,
                        password_hash VARCHAR(128)
                    )
                '''))
                
                # Then create JobApplication table with foreign key
                conn.execute(text('''
                    CREATE TABLE IF NOT EXISTS job_application (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        company VARCHAR(100) NOT NULL,
                        position VARCHAR(100) NOT NULL,
                        application_date DATETIME,
                        status VARCHAR(50),
                        source VARCHAR(50),
                        job_description TEXT,
                        next_followup DATETIME,
                        notes TEXT,
                        FOREIGN KEY(user_id) REFERENCES user(id)
                    )
                '''))
            
            print("✅ Tables created successfully")
            return True
        except Exception as e:
            print(f"❌ Error creating tables: {str(e)}")
            return False

if __name__ == '__main__':
    create_tables()