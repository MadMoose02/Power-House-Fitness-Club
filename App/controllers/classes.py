from App.models import Class
from App.database import db

def create_class(name, instructor, description) -> Class:
    """
    Create a new Class object with the given name and description, and adds it to the database.
    
    Args:
        name (str): The name of the class.
        instructor (str): The instructor of the class.
        description (str): A description of the class.
        
    Returns:
        Class: The newly created Class object.
    """
    
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


def get_classes() -> list[Class]:
    """
    Returns:
        List of Class objects.
    """
    return Class.query.all()
