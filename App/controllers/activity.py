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


def get_activity(id) -> Activity:
    return Activity.query.get(id)


def get_all_activities():
    return Activity.query.all()

def get_all_activities_json():
    return [i.get_json() for i in Activity.query.all()]


def get_all_activities_of_user(user_id):
    return Activity.query.filter_by(user_id=user_id).all()


def get_all_activities_of_user_json(user_id):
    return [i.get_json() for i in get_all_activities_of_user(user_id)]