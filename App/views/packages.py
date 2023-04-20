from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import current_user

from App.models import db
from App.controllers import retrieve_current_user, get_packages

packages_views = Blueprint('packages_views', __name__, template_folder='../templates')

@packages_views.route('/packages', methods=['GET'])
def packages_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    return render_template('packages.html', user=user, packages=get_packages())