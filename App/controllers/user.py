from App.models import User
from App.database import db

def create_user(username, password, fname, lname, dob, address, phone, 
                 sex, email, image, package_id, emergency_contact_id) -> User:
    new_user = User(
        username=username, 
        password=password, 
        fname=fname, 
        lname=lname,
        dob=dob, 
        address=address, 
        phone=phone, 
        sex=sex, 
        email=email,
        image=image,
        package_id=package_id,
        emergency_contact_id=emergency_contact_id
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

def update_user_data(user_id, data: User) -> bool:
    user = get_user(user_id)
    if not user: return False
    user = data
    db.session.add(user)
    db.session.commit()
    return True