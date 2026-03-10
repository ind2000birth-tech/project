import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key-change-in-prod')

    # Session cookie settings – required for login to persist on Vercel (HTTPS)
    SESSION_COOKIE_SECURE = True       # Only send cookie over HTTPS
    SESSION_COOKIE_SAMESITE = 'Lax'   # Protect against CSRF while allowing normal navigation
    SESSION_COOKIE_HTTPONLY = True     # Prevent JS access to cookie
    
    db_url = os.getenv('DATABASE_URL', '')
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    # Fall back to a SQLite file only for local dev; Vercel needs DATABASE_URL set
    SQLALCHEMY_DATABASE_URI = db_url if db_url else 'sqlite:///portfolio.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail settings
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')

    # Admin settings
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')
