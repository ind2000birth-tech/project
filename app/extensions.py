from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager

db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()

# flask_migrate is only needed for local CLI migrations, not on Vercel
try:
    from flask_migrate import Migrate
    migrate = Migrate()
    _use_migrate = True
except ImportError:
    migrate = None
    _use_migrate = False

def init_extensions(app):
    db.init_app(app)
    if _use_migrate and migrate:
        migrate.init_app(app, db)
    mail.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'admin_bp.login'
    login_manager.login_message_category = 'info'
