from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db

profile_views = Blueprint('profile_views', __name__, template_folder='../templates')

@profile_views.route('/profile', methods=['GET'])
def profile_page():
    return render_template('profile.html')