from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import current_user, login_required

from App.models import db
from App.controllers import retrieve_current_user, get_packages, get_package

transaction_views = Blueprint('transaction_views', __name__, template_folder='../templates')

@transaction_views.route('/transactions', methods=['GET'])
@login_required
def transactions_history_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    user_package = get_package(user.package_id).get_json() if user else None
    return render_template('transaction-history.html', user=user, user_package=user_package)