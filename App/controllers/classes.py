from App.models import Class
from App.database import db

def create_class(name, instructor, description, filename, package) -> Class:
    new_class = Class(
        name=name,
        instructor=instructor,
        desc=description,
        filename=filename,
        package=package
    )
    db.session.add(new_class)
    db.session.commit()
    return new_class


def create_classes(classes: dict) -> None:
    for class_ in classes:
        create_class(
            class_['name'], 
            class_['instructor'], 
            class_['description'], 
            class_['filename'], 
            ", ".join(class_['package'])
        )


def get_class(id) -> Class:
    return Class.query.get(id)


def get_all_classes():
    return Class.query.all()


def get_all_classes_json():
    return [class_.get_json() for class_ in get_all_classes()]
