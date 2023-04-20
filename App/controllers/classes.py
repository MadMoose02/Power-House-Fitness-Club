from App.models import Class
from App.database import db

def create_class(name, description) -> Class:
    """
    Create a new Class object with the given name and description, and adds it to the database.
    
    Args:
        name (str): The name of the class.
        description (str): A description of the class.
        
    Returns:
        Class: The newly created Class object.
    """
    
    new_class = Class(
        name=name,
        description=description
    )
    db.session.add(new_class)
    db.session.commit()
    return new_class


def get_classes():
    """
    Returns:
    List of Class objects.
    """
    return Class.query.all()
