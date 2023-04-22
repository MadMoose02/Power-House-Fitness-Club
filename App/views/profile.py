from os import path
from datetime import date
from base64 import b64encode
from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import current_user, login_required

from App.models import db, User
from App.controllers import (
    get_packages,
    get_emergency_contact,
    get_user,
    update_user_data,
    get_package,
    username_exists
)

profile_views = Blueprint('profile_views', __name__, template_folder='../templates')

@profile_views.route('/profile', methods=['GET'])
@login_required
def profile_page():
    return render_template(
        'profile.html', 
        user=current_user,
        user_package=get_package(current_user.package_id).get_json(),
        packages=get_packages(),
        emergency_contact=get_emergency_contact(current_user.emergency_contact_id).get_json()
    )
    
    
@profile_views.route('/api/update-user', methods=['POST'])
@login_required
def update_user():
    try:
        if request.form['password'] != request.form['password-repeat']:
            flash('Passwords do not match', category='error')
            return redirect(url_for('profile_views.profile_page'))
        
        if request.form['username'] != current_user.username:
            if username_exists(request.form['username']):
                flash('Username already exists', category='error')
                return redirect(url_for('profile_views.profile_page'))
        
        username = request.form['username']
        password = request.form['password']
        fname = request.form['firstname']
        lname = request.form['lastname']
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

        update_user_data(current_user.id, curr_user)
        flash('Profile updated', category='info')
        
    except Exception as e:
        db.rollback()
        flash("Unable to register", category='error')
    
    return redirect(url_for('profile_views.profile_page'))