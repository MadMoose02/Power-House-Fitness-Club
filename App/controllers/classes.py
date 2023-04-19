from App.models import Class
from App.database import db

def create_class(name, description):
    """
    Create a new Class object with the given name and description, add it to
    the database session, and commit the changes. Returns the newly created
    Class object.
    Args:
        name (str): The name of the new Class.
        description (str): A description of the new Class.
    Returns:
        Class: The newly created Class object.
    """
    newclass = Class(
        name=name,
        description=description
    )
    db.session.add(newclass)
    db.session.commit()
    return newclass


