from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db

classes_views = Blueprint('classes_views', __name__, template_folder='../templates')

@classes_views.route('/classes', methods=['GET'])
def classes_page():
    return render_template('classes.html')