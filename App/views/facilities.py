from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db

facilities_views = Blueprint('facilities_views', __name__, template_folder='../templates')

@facilities_views.route('/facilities', methods=['GET'])
def facilities_page():
    return render_template('facilities.html')