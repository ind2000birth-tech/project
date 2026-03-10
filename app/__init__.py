from flask import Flask
from app.config import Config
from app.extensions import db, migrate, mail, login_manager, init_extensions

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    init_extensions(app)
    
    # Register blueprints
    from app.routes.home_routes import home_bp
    from app.routes.about_routes import about_bp
    from app.routes.experience_routes import experience_bp
    from app.routes.project_routes import project_bp
    from app.routes.contact_routes import contact_bp
    from app.routes.admin_routes import admin_bp
    
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(experience_bp)
    app.register_blueprint(project_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(admin_bp)

    # Auto-create tables and seed admin user on first startup (critical for Vercel)
    with app.app_context():
        db.create_all()
        from app.services.auth_service import AuthService
        admin_user = app.config.get('ADMIN_USERNAME', 'admin')
        admin_pass = app.config.get('ADMIN_PASSWORD', 'admin123')
        AuthService.create_initial_admin(admin_user, admin_pass)
    
    return app
