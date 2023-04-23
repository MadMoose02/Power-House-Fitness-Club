from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import current_user

from App.models import db
from App.controllers import retrieve_current_user, get_all_facilities_json, get_package

facilities_views = Blueprint('facilities_views', __name__, template_folder='../templates')

@facilities_views.route('/facilities', methods=['GET'])
def facilities_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    user_package = get_package(user.package_id).get_json() if user else None
    num_to_display = 2
    return render_template(
        'facilities.html', 
        user=user, 
        user_package=user_package, 
        facilities=get_all_facilities_json(),
        num_to_display=num_to_display,
        flen = len(get_all_facilities_json())
    )