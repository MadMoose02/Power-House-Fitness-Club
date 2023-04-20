from App.models import Package
from App.database import db

def create_package(type, price, desc) -> Package:
    """
    Creates a new Package object with given type, price and description and adds it to the database.

    Args:
        type (str): The type/identifier of the package.
        price (float): The price of the package.
        desc (str): A description of the package.

    Returns:
        Package: The newly created Package object.
    """
    
    new_package = Package(
        type=type,
        price=price,
        description=desc
    )
    db.session.add(new_package)
    db.session.commit()
    return new_package

