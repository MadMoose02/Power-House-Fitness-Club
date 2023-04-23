from App.models import Discussion
from App.database import db

def create_discussion(title, started_by) -> Discussion:
    new_discussion = Discussion(title=title, started_by=started_by)
    db.session.add(new_discussion)
    db.session.commit()
    return new_discussion


def get_discussion(id) -> Discussion:
    return Discussion.query.get(id)


def get_all_discussions() -> list[Discussion]:
    return Discussion.query.all()


def get_discussions_by_user(user_id) -> list[Discussion]:
    return Discussion.query.filter_by(started_by=user_id).all()


def get_discussions_by_title(title) -> list[Discussion]:
    return Discussion.query.filter_by(title=title).all()