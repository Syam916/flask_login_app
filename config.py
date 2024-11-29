import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')  # Default for development
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://username:password@localhost/your_database')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
