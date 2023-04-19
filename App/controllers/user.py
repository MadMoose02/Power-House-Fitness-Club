from App.models import User
from App.database import db

def create_user(username, password, fname, lname, dob, address, phone, sex, email) -> User:
    """
    Create a new user and add it to the database.

    :param username: A string representing the username of the new user.
    :param password: A string representing the password of the new user.
    :param fname: A string representing the first name of the new user.
    :param lname: A string representing the last name of the new user.
    :param dob: A string representing the date of birth of the new user.
    :param address: A string representing the address of the new user.
    :param phone: A string representing the phone number of the new user.
    :param sex: A string representing the sex of the new user.
    :param email: A string representing the email address of the new user.
    :return: A User object representing the newly created user.
    """
    newuser = User(
        username=username, 
        password=password, 
        fname=fname, 
        lname=lname,
        dob=dob, 
        address=address, 
        phone=phone, 
        sex=sex, 
        email=email
    )
    db.session.add(newuser)
    db.session.commit()
    return newuser


def get_user_by_username(username) -> User:
    return User.query.filter_by(username=username).first()

def get_user(id) -> User:
    return User.query.get(id)

def get_all_users() -> list[User]:
    return User.query.all()

def get_all_users_json() -> list[dict]:
    users = User.query.all()
    if not users: return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username) -> bool:
    user = get_user(id)
    if not user: return False
    user.username = username
    db.session.add(user)
    db.session.commit()
    return True
    