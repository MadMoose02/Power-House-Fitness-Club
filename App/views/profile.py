from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import current_user, login_required

from App.models import db
from App.controllers import get_packages, get_emergency_contact

profile_views = Blueprint('profile_views', __name__, template_folder='../templates')

@profile_views.route('/profile', methods=['GET'])
@login_required
def profile_page():
    return render_template(
        'profile.html', 
        user=current_user, 
        packages=get_packages(), 
        emergency_contact=get_emergency_contact(current_user.emergency_contact_id).get_json()
    )