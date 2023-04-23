from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import current_user

from App.models import db
from App.controllers import retrieve_current_user, get_all_packages_json, get_package

packages_views = Blueprint('packages_views', __name__, template_folder='../templates')

@packages_views.route('/packages', methods=['GET'])
def packages_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    user_package = get_package(user.package_id).get_json() if user else None
    return render_template(
        'packages.html', 
        user=user, 
        user_package=user_package, 
        packages=get_all_packages_json()
    )