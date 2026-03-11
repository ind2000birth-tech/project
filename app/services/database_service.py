from app.extensions import db

class DatabaseService:
    @staticmethod
    def add_item(item):
        try:
            db.session.add(item)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error adding item: {e}")
            return False

    @staticmethod
    def update_item(item=None):
        try:
            if item:
                db.session.add(item)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error updating item: {e}")
            return False

    @staticmethod
    def delete_item(item):
        try:
            db.session.delete(item)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting item: {e}")
            return False

    @staticmethod
    def get_all(model):
        return model.query.order_by(model.created_at.desc()).all()

    @staticmethod
    def get_by_id(model, item_id):
        return model.query.get(item_id)
