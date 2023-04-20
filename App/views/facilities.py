from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import current_user

from App.models import db
from App.controllers import retrieve_current_user, get_facilities

facilities_views = Blueprint('facilities_views', __name__, template_folder='../templates')

@facilities_views.route('/facilities', methods=['GET'])
def facilities_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    return render_template('facilities.html', user=user, facilities=get_facilities())