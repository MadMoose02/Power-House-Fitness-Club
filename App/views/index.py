from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import login_required, current_user
from datetime import date
from App.models import db
from App.controllers import create_user, get_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def home_page():
    
    # Check if user is logged in
    if not current_user.is_authenticated:
        return render_template('index.html', user=None)
    
    user = retrieve_current_user()
    print("Rendering home page with navbar profile for:", user.username)
    
    return render_template('index.html', user=user)


@login_required
def retrieve_current_user():
    return get_user(current_user.id)

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user(
        'david', 
        'davidpass', 
        'David', 
        'Bossman', 
        date(1998, 9, 30), 
        '#9 Avenue Street', 
        '123545452', 
        'male', 
        'david.bossman@mail.com'
    )
    return jsonify(message='db initialised!')


@index_views.route('/healthcheck', methods=['GET'])
def health_check():
    return jsonify(message='healthy', status=200)