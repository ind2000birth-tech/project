from app.models.user_model import User
from app.extensions import db

class AuthService:
    @staticmethod
    def authenticate_admin(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return user
        return None

    @staticmethod
    def create_initial_admin(username, password):
        if not User.query.filter_by(username=username).first():
            admin = User(username=username)
            admin.set_password(password)
            db.session.add(admin)
            db.session.commit()
            return True
        return False
