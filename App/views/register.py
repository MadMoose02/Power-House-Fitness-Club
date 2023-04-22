from os import path
from datetime import date
from base64 import b64encode
from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import current_user

from App.models import db, User
from App.controllers import (
    retrieve_current_user, 
    get_packages,
    get_package,
    get_all_users,
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
    return render_template('register.html', user=user, user_package=user_package, packages=get_packages())


@register_views.route('/register', methods=['POST'])
def register():
    print(request.form.to_dict())
    try:
        if request.form['password'] != request.form['password-repeat']:
            flash('Passwords do not match', category='error')
            return redirect(url_for('register_views.register_page'))
        
        password = request.form['password']
        fname = request.form['firstname']
        lname = request.form['lastname']
        num = len(get_same_names(fname, lname))
        username = f"{fname.lower()}.{lname.lower()}{str(num) if num > 0 else ''}"
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
        create_emergency_contact(
            fname=em_contact_fname,
            lname=em_contact_lname,
            relation=en_contact_relationship,
            contact=em_contact_contact
        )
        emergency_contact_id = get_emergency_contact(len(get_all_emergency_contacts())).id

        # Add new user
        create_user(
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

        flash('Registration complete. Account created successfully', category='info')
        
    except Exception as e:
        db.rollback()
        flash("Unable to register", category='error')
    
    return redirect(url_for('index_views.home_page'))