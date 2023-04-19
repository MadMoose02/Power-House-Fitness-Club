from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db

register_views = Blueprint('register_views', __name__, template_folder='../templates')

@register_views.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')