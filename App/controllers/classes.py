from App.models import Class
from App.database import db

def create_class(name, instructor, description) -> Class:
    new_class = Class(
        name=name,
        instructor=instructor,
        desc=description
    )
    db.session.add(new_class)
    db.session.commit()
    return new_class


def create_classes(classes: dict) -> None:
    for class_ in classes:
        create_class(class_['name'], class_['instructor'], class_['description'])


def get_class(id) -> Class:
    return Class.query.get(id)


def get_classes() -> list[Class]:
    return Class.query.all()
