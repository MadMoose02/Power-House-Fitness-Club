from App.models import Package
from App.database import db

def create_package(type, price, description) -> Package:
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


def get_package(id) -> Package:
    return Package.query.get(id)


def get_packages() -> list[Package]:
    return Package.query.all()