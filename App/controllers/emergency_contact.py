from App.models import EmergencyContact
from App.database import db

def create_emergency_contact(fname, lname, relation, contact) -> EmergencyContact:
    new_emergency_contact = EmergencyContact(
        fname=fname, 
        lname=lname,
        relation=relation, 
        contact=contact
    )
    db.session.add(new_emergency_contact)
    db.session.commit()
    return new_emergency_contact


def create_emergency_contacts(emergency_contacts) -> None:
    for contact in emergency_contacts:
        create_emergency_contact(
            contact['fname'], 
            contact['lname'], 
            contact['relation'], 
            contact['contact']
        )
