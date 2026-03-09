from app import create_app
from app.extensions import db
from app.services.auth_service import AuthService
import os

app = create_app()

def init_db():
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        
        admin_user = os.getenv('ADMIN_USERNAME', 'admin')
        admin_pass = os.getenv('ADMIN_PASSWORD', 'admin123')
        
        print(f"Creating initial admin user: {admin_user}")
        if AuthService.create_initial_admin(admin_user, admin_pass):
            print("Admin user created successfully!")
        else:
            print("Admin user already exists.")
            
        print("Database initialization complete.")

if __name__ == "__main__":
    init_db()
