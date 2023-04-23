from .index import index_views
from .auth import auth_views
from .facilities import facilities_views
from .packages import packages_views
from .classes import classes_views
from .about import about_views
from .register import register_views
from .profile import profile_views
from .wallet import wallet_views
from .activity import activity_views
from .transaction import transaction_views

views = [
    index_views, 
    auth_views, 
    facilities_views, 
    packages_views, 
    classes_views, 
    about_views, 
    register_views, 
    profile_views,
    wallet_views,
    activity_views,
    transaction_views
]