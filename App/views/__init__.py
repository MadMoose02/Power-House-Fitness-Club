# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .facilities import facilities_views
from .packages import packages_views
from .classes import classes_views
from .about import about_views
from .login import login_views
from .register import register_views
from .profile import profile_views

views = [
    user_views, 
    index_views, 
    auth_views, 
    facilities_views, 
    packages_views, 
    classes_views, 
    about_views, 
    login_views, 
    register_views, 
    profile_views
]