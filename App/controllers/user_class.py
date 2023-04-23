from App.models import UserClass
from App.database import db

def create_userclass(user_id, class_id, class_name) -> UserClass:
    new_userclass = UserClass(
        user_id=user_id,
        class_id=class_id,
        class_name=class_name
    )
    db.session.add(new_userclass)
    db.session.commit()
    return new_userclass


def get_userclass(id) -> UserClass:
    return UserClass.query.get(id)


def get_userclasses_by_user_id(user_id) -> list[UserClass]:
    return UserClass.query.filter_by(user_id=user_id).all()


def get_all_userclasses() -> list[UserClass]:
    return UserClass.query.all()


def get_all_userclasses_json() -> list[dict]:
    return [userclass.get_json() for userclass in get_all_userclasses()]


def delete_userclass(user_id, class_id) -> None:
    userclass = UserClass.query.filter_by(user_id=user_id, class_id=class_id).first()
    db.session.delete(userclass)
    db.session.commit()