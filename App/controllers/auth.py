from flask_login import login_required, login_user, login_manager, logout_user, LoginManager, current_user
from flask_jwt_extended import create_access_token, jwt_required, JWTManager

from App.controllers import ( get_user )
from App.models import User

def jwt_authenticate(username, password) -> str:
    user = None
    if '@' in username: user = User.query.filter_by(email=username).first()
    else: user = User.query.filter_by(username=username).first()
    if not user: return None
    if not user.check_password(password): return None
    return create_access_token(identity=username)


@login_required
def retrieve_current_user():
    return get_user(current_user.id)

def login(username: str, password: str) -> User:
    user = User.query.filter_by(username=username).first()
    if not user: user = User.query.filter_by(email=username).first()
    if not user: return None
    if not user.check_password(password): return None
    print("Password check passed")
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