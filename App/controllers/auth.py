from flask_login import login_user, login_manager, logout_user, LoginManager
from flask_jwt_extended import create_access_token, jwt_required, JWTManager

from App.models import User

def jwt_authenticate(username, password) -> str:
    """
    Authenticates a user with a JWT.

    :param username: The username of the user.
    :type username: str
    :param password: The password of the user.
    :type password: str
    :return: Returns an access token if the authentication is successful, otherwise returns None.
    :rtype: str or None
    """
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password): return None
    return create_access_token(identity=username)


def login(username: str, password: str) -> User:
    """
    Logs in a user with the given credentials.

    :param username: The username of the user.
    :param password: The password of the user.
    :return: An instance of the User class representing the logged in user,
             or None if the credentials are invalid.
    """
    user = User.query.filter_by(username=username).first()
    if not user and not user.check_password(password): return None
    return user


def setup_flask_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    return login_manager

def setup_jwt(app):
    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(identity):
        user = User.query.filter_by(username=identity).one_or_none()
        if user:
            return user.id
        return None

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.get(identity)

    return jwt