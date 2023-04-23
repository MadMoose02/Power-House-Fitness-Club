from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from App.models import db
from App.controllers import retrieve_current_user, get_package

activity_views = Blueprint('activity_views', __name__, template_folder='../templates')

@activity_views.route('/log-activity', methods=['GET'])
@login_required
def log_activity_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    user_package = get_package(user.package_id).get_json() if user else None
    return render_template('log-activity.html', user=user, user_package=user_package)


@activity_views.route('/log-activity', methods=['POST'])
@login_required
def add_activity_log():
    print(request.form.to_dict())
    return redirect(url_for('activity_views.log_activity_page'))


@activity_views.route('/activty-tracking', methods=['GET'])
@login_required
def activty_tracking_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    user_package = get_package(user.package_id).get_json() if user else None
    return render_template('activtiy-tracking.html', user=user, user_package=user_package)