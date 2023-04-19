from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import current_user

from App.models import db
from App.controllers import retrieve_current_user

register_views = Blueprint('register_views', __name__, template_folder='../templates')

@register_views.route('/register', methods=['GET'])
def register_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    return render_template('register.html', user=user)