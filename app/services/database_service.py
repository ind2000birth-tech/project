from app.extensions import db

class DatabaseService:
    @staticmethod
    def add_item(item):
        db.session.add(item)
        db.session.commit()

    @staticmethod
    def update_item(item=None):
        if item:
            db.session.add(item)
        db.session.commit()

    @staticmethod
    def delete_item(item):
        db.session.delete(item)
        db.session.commit()

    @staticmethod
    def get_all(model):
        return model.query.order_by(model.created_at.desc()).all()

    @staticmethod
    def get_by_id(model, item_id):
        return model.query.get(item_id)
