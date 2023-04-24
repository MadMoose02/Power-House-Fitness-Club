from App.models import Facility
from App.database import db

def create_facility(name, description, filename, package) -> Facility:
    new_facility = Facility(
        name=name,
        desc=description,
        filename=filename,
        package=package
    )
    db.session.add(new_facility)
    db.session.commit()
    return new_facility


def create_facilities(facilities):
    for facility in facilities:
        create_facility(
            facility['name'], 
            facility['description'], 
            facility['filename'], 
            ", ".join(facility['package'])
        )


def get_facility(id) -> Facility:
    return Facility.query.get(id)


def get_all_facilities():
    return Facility.query.all()


def get_all_facilities_json():
    return [facility.get_json() for facility in get_all_facilities()]