from app import create_app, db
from sqlalchemy import text

def initialize_database():
    app = create_app()
    with app.app_context():
        try:
            # For SQLite: disable foreign key constraints temporarily
            if db.engine.name == 'sqlite':
                with db.engine.connect() as conn:
                    conn.execute(text('PRAGMA foreign_keys=OFF'))
                    db.create_all()
                    conn.execute(text('PRAGMA foreign_keys=ON'))
            else:
                db.create_all()
            
            print("✅ Database tables created successfully")
            return True
        except Exception as e:
            print(f"❌ Error creating tables: {str(e)}")
            return False

if __name__ == '__main__':
    initialize_database()