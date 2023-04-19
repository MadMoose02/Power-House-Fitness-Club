from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db

about_views = Blueprint('about_views', __name__, template_folder='../templates')

@about_views.route('/about', methods=['GET'])
def about_page():
    return render_template('about.html')