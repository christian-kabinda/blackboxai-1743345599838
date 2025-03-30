import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LINKEDIN_API_KEY = os.environ.get('LINKEDIN_API_KEY')
    INDEED_API_KEY = os.environ.get('INDEED_API_KEY')
    GMAIL_CLIENT_ID = os.environ.get('GMAIL_CLIENT_ID')
    GMAIL_CLIENT_SECRET = os.environ.get('GMAIL_CLIENT_SECRET')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')