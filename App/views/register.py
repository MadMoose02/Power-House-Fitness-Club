from os import path
from datetime import date
from base64 import b64encode
from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import current_user

from App.models import db, User
from App.controllers import (
    retrieve_current_user, 
    get_all_packages_json,
    get_package,
    create_emergency_contact,
    get_emergency_contact,
    get_all_emergency_contacts,
    create_user,
    get_same_names
)

register_views = Blueprint('register_views', __name__, template_folder='../templates')

@register_views.route('/register', methods=['GET'])
def register_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    user_package = get_package(user.package_id).get_json() if user else None
    return render_template(
        'register.html', 
        user=user, 
        user_package=user_package, 
        packages=get_all_packages_json()
    )


@register_views.route('/register', methods=['POST'])
def register():
    print(request.form.to_dict())
    try:
        if request.form['password'] != request.form['password-repeat']:
            flash('Passwords do not match', category='error')
            return redirect(url_for('register_views.register_page'))
        
        fname = request.form['firstname']
        lname = request.form['lastname']
        num = len(get_same_names(fname, lname))
        username = f"{fname.lower()}.{lname.lower()}{str(num) if num > 0 else ''}"
        dob = date(
            year=int(request.form['dob'].split('-')[0]), 
            month=int(request.form['dob'].split('-')[1]), 
            day=int(request.form['dob'].split('-')[2])
        )
        image = b64encode(request.files['image'].read()) if request.files['image'] else None
        
        # If image is not provided, use default image for sex of user
        if image is None:
            if request.form['sex'] == "other":  image = "App/static/images/user/default-user.png"
            elif request.form['sex'] == "male": image = "App/static/images/user/male.jpg"
            else: image = "App/static/images/user/female.jpg"
            image = b64encode(open(path.join(path.dirname(__file__).split('App')[0], image), 'rb').read())
        
        # Add emergency contact first
        create_emergency_contact(
            fname=request.form['emgcy-fname'],
            lname=request.form['emgcy-lname'],
            relation=request.form['relationship'],
            contact=request.form['emgcy-contactno']
        )
        emergency_contact_id = get_emergency_contact(len(get_all_emergency_contacts())).id

        # Add new user
        create_user(
            username=username,
            password=request.form['password'],
            fname=request.form['firstname'],
            lname=request.form['lastname'],
            dob=dob,
            address=request.form['address'],
            phone=request.form['contactno'],
            sex=request.form['sex'],
            email=request.form['email'],
            image=image,
            package_id=request.form['package-id'],
            emergency_contact_id=emergency_contact_id
        )

        flash('Registration complete. Account created successfully', category='info')
        
    except Exception as e:
        db.session.rollback()
        flash("Unable to register", category='error')
    
    return redirect(url_for('index_views.home_page'))