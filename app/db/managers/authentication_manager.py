from sqlalchemy import inspect
from sqlalchemy.orm import Session

from app.db.managers.base_manager import BaseManager
from app.db.models.authentication import Permission
from app.db.session import engine


class TokenManager(BaseManager):

    @staticmethod
    def filter_by_user_id_and_access_token(model, access_token, user_id, db: Session):
        return db.query(model).filter(model.access_token == access_token, model.is_active == True, model.user_id==user_id).first()


class PermissionManager:

    @staticmethod
    def create(data: dict, db):
        breakpoint()
        obj = Permission(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def get_db_table_names():
        inspector = inspect(engine)
        table_names = set(inspector.get_table_names()) - {"permission", "token"}
        return list(table_names)

    @staticmethod
    def get_permission_with_postfix(table_names, postfix):
        return [f"{table_name}: {postfix}" for table_name in table_names]

    @staticmethod
    def get_create_permission(table_names):
        return PermissionManager.get_permission_with_postfix(table_names=table_names, postfix="create")

    @staticmethod
    def get_read_permission(table_names):
        return PermissionManager.get_permission_with_postfix(table_names=table_names, postfix="read")

    @staticmethod
    def get_update_permission(table_names):
        return PermissionManager.get_permission_with_postfix(table_names=table_names, postfix="change")

    @staticmethod
    def get_delete_permission(table_names):
        return PermissionManager.get_permission_with_postfix(table_names=table_names, postfix="delete")

    @staticmethod
    def get_base_permissions():
        tales_name = PermissionManager.get_db_table_names()
        permissions_list = PermissionManager.get_read_permission(tales_name)
        return permissions_list

    @staticmethod
    def create_student_permissions(student_id, db):
        base_permissions = PermissionManager.get_base_permissions()
        data = {"user_id": student_id, "permissions": base_permissions}
        return PermissionManager.create(data, db)

    @staticmethod
    def create_teacher_permissions(teacher_id, db):
        pass

    @staticmethod
    def create_principal_permissions(principal_id, db):
        pass

    @staticmethod
    def create_super_user_permissions(super_user_id, db):
        pass
