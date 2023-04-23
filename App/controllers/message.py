from App.models import Message
from App.database import db

def create_message(discussion_id, user_id, content, external_link, datetime) -> Message:
    new_message = Message(
        discussion_id=discussion_id,
        user_id=user_id,
        content=content,
        external_link=external_link,
        datetime=datetime
    )   
    db.session.add(new_message)
    db.session.commit()
    return new_message


def get_message(id) -> Message:
    return Message.query.get(id)


def get_messages() -> list[Message]:
    return Message.query.all()


def get_messages_by_user(user_id) -> list[Message]:
    return Message.query.filter_by(started_by=user_id).all()


def get_messages_by_discussion(discussion_id) -> list[Message]:
    return Message.query.filter_by(discussion_id=discussion_id).all()