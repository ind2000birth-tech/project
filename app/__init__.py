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
    
    return app
