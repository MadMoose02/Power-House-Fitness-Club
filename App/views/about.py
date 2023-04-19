from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import current_user

from App.models import db
from App.controllers import retrieve_current_user

about_views = Blueprint('about_views', __name__, template_folder='../templates')

@about_views.route('/about', methods=['GET'])
def about_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    return render_template('about.html', user=user)