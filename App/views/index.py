from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from datetime import date
from App.models import db
from App.controllers import create_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def home_page(current_user=None):
    return render_template('index.html', user=current_user)


@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user(
        'bossman_david', 
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