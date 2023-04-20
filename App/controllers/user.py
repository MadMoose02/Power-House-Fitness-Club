from App.models import User
from App.database import db

def create_user(username, password, fname, lname, dob, address, phone, sex, email) -> User:
    """
    Creates a new user object with given params and adds it to the database.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.
        fname (str): The first name of the user.
        lname (str): The last name of the user.
        dob (str): The date of birth of the user in the format of 'YYYY-MM-DD'.
        address (str): The address of the user.
        phone (str): The phone number of the user.
        sex (str): The sex of the user.
        email (str): The email of the user.

    Returns:
        User: The newly created User object.
    """
    
    new_user = User(
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
    db.session.add(new_user)
    db.session.commit()
    return new_user


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
    