from App.models import Facility
from App.database import db

def create_facility(name, description) -> Facility:
    new_facility = Facility(
        name=name,
        desc=description
    )
    db.session.add(new_facility)
    db.session.commit()
    return new_facility


def create_facilities(facilities):
    for facility in facilities:
        create_facility(facility['name'], facility['description'])


def get_facility(id) -> Facility:
    return Facility.query.get(id)


def get_facilities() -> list[Facility]:
    return Facility.query.all()