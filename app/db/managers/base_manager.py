from sqlalchemy.orm import Session


class BaseManager:

    @staticmethod
    def create(model, data, db: Session):
        obj = model(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def fetch_all(model, db: Session):
        return db.query(model).filter(model.is_active == True).all()

    @staticmethod
    def get_by_id(model, obj_id, db: Session):
        return db.query(model).filter(model.id == obj_id, model.is_active == True).first()

    @staticmethod
    def update(model, obj_id, data, db: Session):
        obj = db.query(model).filter(model.id == obj_id, model.is_active == True).first()
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db.commit()
            db.refresh(obj)
            return obj
        return None

    @staticmethod
    def delete_by_id(model, obj_id, db: Session):
        obj = db.query(model).filter(model.id == obj_id, model.is_active == True).first()
        if obj:
            setattr(obj, "is_active", False)
            db.commit()
            db.refresh(obj)
            return obj
        return None
