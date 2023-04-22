from os import path
from datetime import date
from base64 import b64encode
from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views
from App.models import db
from App.controllers import (
    create_user,
    create_emergency_contact,
    get_emergency_contact,
    get_all_emergency_contacts,
    jwt_authenticate, 
    get_user,
    get_all_users,
    get_all_users_json
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)