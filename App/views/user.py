from os import path
from datetime import date
from base64 import b64encode
from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views
from App.models import db
from App.controllers import (
    create_user,
    create_emergency_contact,
    get_emergency_contact,
    get_all_emergency_contacts,
    jwt_authenticate, 
    get_user,
    get_all_users,
    get_all_users_json
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/register', methods=['POST'])
def register():
    print(__file__)
    try:
        if request.form['password'] != request.form['password-repeat']:
            flash('Passwords do not match', category='error')
            return redirect(url_for('register_views.register_page'))
        
        password = request.form['password']
        fname = request.form['firstname']
        lname = request.form['lastname']
        username = f"{fname.lower()}.{lname.lower()}{str(len(get_all_users()))}"
        dob = date(
            year=int(request.form['dob'].split('-')[0]), 
            month=int(request.form['dob'].split('-')[1]), 
            day=int(request.form['dob'].split('-')[2])
        )
        address = request.form['address']
        phone = request.form['contactno']
        sex = request.form['sex']
        email = request.form['email']
        image = b64encode(request.files['image'].read()) if request.files['image'] else None
        package_id = request.form['package-id']
        
        # If image is not provided, use default image for sex of user
        if image is None:
            if sex == "other":  image = "App/static/images/default-user.png"
            elif sex == "male": image = "App/static/images/male.jpg"
            else: image = "App/static/images/female.jpg"
            image = b64encode(open(path.join(path.dirname(__file__).split('App')[0], image), 'rb').read())
        
        # Collect emergency contact info
        em_contact_fname = request.form['emgcy-fname']
        em_contact_lname = request.form['emgcy-lname']
        en_contact_relationship = request.form['relationship']
        em_contact_contact = request.form['emgcy-contactno']
        
        # Add emergency contact first
        new_emergency_contact = create_emergency_contact(
            fname=em_contact_fname,
            lname=em_contact_lname,
            relation=en_contact_relationship,
            contact=em_contact_contact
        )
        db.session.add(new_emergency_contact)
        emergency_contact_id = get_emergency_contact(len(get_all_emergency_contacts())).id

        # Add new user
        new_user = create_user(
            username=username,
            password=password,
            fname=fname,
            lname=lname,
            dob=dob,
            address=address,
            phone=phone,
            sex=sex,
            email=email,
            image=image,
            package_id=package_id,
            emergency_contact_id=emergency_contact_id
        )

        db.session.add(new_user)
        db.session.commit()
        flash('Registration complete. Account created successfully', category='info')
        
    except Exception as e:
        db.rollback()
        flash("Unable to register", category='error')
    
    return redirect(url_for('index_views.home_page'))


@user_views.route('/api/update-user', methods=['POST'])
@login_required
def update_user():
    try:
        if request.form['password'] != request.form['password-repeat']:
            flash('Passwords do not match', category='error')
            return redirect(url_for('profile_views.profile_page'))
        
        password = request.form['password']
        fname = request.form['firstname']
        lname = request.form['lastname']
        username = f"{fname.lower()}.{lname.lower()}{str(len(get_all_users()))}"
        dob = date(
            year=int(request.form['dob'].split('-')[0]), 
            month=int(request.form['dob'].split('-')[1]), 
            day=int(request.form['dob'].split('-')[2])
        )
        address = request.form['address']
        phone = request.form['contactno']
        sex = request.form['sex']
        email = request.form['email']
        package_id = request.form['package-id']
        
        # Collect emergency contact info
        em_contact_fname = request.form['emgcy-fname']
        em_contact_lname = request.form['emgcy-lname']
        en_contact_relationship = request.form['relationship']
        em_contact_contact = request.form['emgcy-contactno']
        
        # Get user from database
        curr_user = get_user(current_user.id)
        image = b64encode(request.files['image'].read()) if request.files['image'] else curr_user.image
        
        # Get emergency contact from database
        emergency_contact = get_emergency_contact(curr_user.emergency_contact_id)

        # Update user information
        curr_user.username=username
        curr_user.password=password
        curr_user.fname=fname
        curr_user.lname=lname
        curr_user.dob=dob
        curr_user.address=address
        curr_user.phone=phone
        curr_user.sex=sex
        curr_user.email=email
        curr_user.image=image
        curr_user.package_id=package_id
        
        # Update emergency contact information
        emergency_contact.fname=em_contact_fname
        emergency_contact.lname=em_contact_lname
        emergency_contact.relation=en_contact_relationship
        emergency_contact.contact=em_contact_contact

        db.session.add(curr_user)
        db.session.add(emergency_contact)
        db.session.commit()
        flash('Profile upadated', category='info')
        
    except Exception as e:
        db.rollback()
        flash("Unable to register", category='error')
    
    return redirect(url_for('profile_views.profile_page'))


@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)
