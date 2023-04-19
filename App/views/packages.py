from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db

packages_views = Blueprint('packages_views', __name__, template_folder='../templates')

@packages_views.route('/packages', methods=['GET'])
def packages_page():
    return render_template('packages.html')