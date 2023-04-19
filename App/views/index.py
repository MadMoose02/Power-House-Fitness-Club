from datetime import date
from flask import Blueprint, redirect, render_template, send_from_directory, jsonify, flash, url_for
from flask_login import current_user

from App.models import db
from App.controllers import create_user, retrieve_current_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def home_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    return render_template('index.html', user=user)


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
    create_user(
        'bob', 
        'bobpass', 
        'Bob', 
        'the Builder', 
        date(1900, 1, 15), 
        '#10A Nickelodeon Road', 
        '123545452', 
        'male',
        'bob.thebuilder@mail.com'
    )
    flash('db initialised!')
    return redirect(url_for('index_views.home_page'))


@index_views.route('/healthcheck', methods=['GET'])
def health_check():
    return jsonify(message='healthy', status=200)