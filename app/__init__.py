from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates')

    app.config.from_object('config.Config')
    db.init_app(app)
    
    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create tables
        
    return app
