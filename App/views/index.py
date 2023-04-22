from flask import Blueprint, render_template, jsonify
from flask_login import current_user

from App.models import db
from App.controllers import retrieve_current_user, get_package

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def home_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    user_package = get_package(user.package_id).get_json() if user else None
    return render_template('index.html', user=user, user_package=user_package)


@index_views.route('/healthcheck', methods=['GET'])
def health_check():
    return jsonify(message='healthy', status=200)