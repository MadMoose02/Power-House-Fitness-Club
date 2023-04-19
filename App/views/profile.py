from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import current_user

from App.models import db
from App.controllers import retrieve_current_user

profile_views = Blueprint('profile_views', __name__, template_folder='../templates')

@profile_views.route('/profile', methods=['GET'])
def profile_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    return render_template('profile.html', user=user)