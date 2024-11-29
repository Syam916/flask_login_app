class Config:
    # Flask settings
    SECRET_KEY = 'your_secret_key'  # Replace with a strong secret key

    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/deployement'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking
