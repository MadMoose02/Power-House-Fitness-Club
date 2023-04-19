from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db

login_views = Blueprint('login_views', __name__, template_folder='../templates')

@login_views.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')