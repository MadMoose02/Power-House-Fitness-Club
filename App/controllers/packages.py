from App.models import Package
from App.database import db

def create_package(type, price, description) -> Package:
    """
    Creates a new Package object with given type, price and description and adds it to the database.

    Args:
        type (str): The type/identifier of the package.
        price (float): The price of the package.
        description (str): A description of the package.

    Returns:
        Package: The newly created Package object.
    """
    
    new_package = Package(
        type=type,
        price=price,
        desc=description
    )
    db.session.add(new_package)
    db.session.commit()
    return new_package


def create_packages(packages):
    for package in packages:
        create_package(package['type'], package['price'], package['description'])


def get_packages() -> list[Package]:
    """
    Returns:
        List of Package objects.
    """
    return Package.query.all()