from App.models import Facility
from App.database import db

def create_facility(name, description, filename) -> Facility:
    new_facility = Facility(
        name=name,
        desc=description,
        filename=filename
    )
    db.session.add(new_facility)
    db.session.commit()
    return new_facility


def create_facilities(facilities):
    for facility in facilities:
        create_facility(facility['name'], facility['description'], facility['filename'])


def get_facility(id) -> Facility:
    return Facility.query.get(id)


def get_all_facilities() -> list[Facility]:
    return Facility.query.all()


def get_all_facilities_json() -> list[dict]:
    return [facility.get_json() for facility in get_all_facilities()]