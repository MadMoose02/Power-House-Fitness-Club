from App.models import Activity
from App.database import db


def create_activity(user_id, date, pre_workout, energy_level, details) -> Activity:
    new_activity = Activity(
        user_id=user_id, 
        date=date, 
        pre_workout=pre_workout, 
        energy_level=energy_level, 
        details=details
    )
    db.session.add(new_activity)
    db.session.commit()
    return new_activity