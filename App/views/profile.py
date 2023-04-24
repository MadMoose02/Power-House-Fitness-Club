from os import path
from datetime import date, datetime
from base64 import b64encode
from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import current_user, login_required

from App.models import db, User
from App.controllers import (
    get_all_packages_json,
    get_emergency_contact,
    get_user,
    update_user_data,
    get_package,
    get_all_packages_json,
    get_all_classes_json,
    username_exists,
    delete_userclass,
    create_userclass,
    get_userclasses_by_user_id,
    create_transaction,
    add_credit,
    add_debit,
    get_userclass
)

profile_views = Blueprint('profile_views', __name__, template_folder='../templates')

@profile_views.route('/profile', methods=['GET'])
@login_required
def profile_page():
    return render_template(
        'profile.html', 
        user=current_user,
        user_package=get_package(current_user.package_id).get_json()
    )
    
    
@profile_views.route('/profile/edit-user', methods=['GET'])
@login_required
def edit_profile_page():
    return render_template(
        'edit-user.html', 
        user=current_user,
        user_package=get_package(current_user.package_id).get_json(),
        packages=get_all_packages_json(),
        emergency_contact=get_emergency_contact(current_user.emergency_contact_id).get_json()
    )
    

@profile_views.route('/profile/edit-classes', methods=['GET'])
@login_required
def edit_classes_page():
    user_classes = [i.get_json()['class_name'] for i in get_userclasses_by_user_id(current_user.id)]
    print(user_classes)
    return render_template(
        'edit-classes.html', 
        user=current_user,
        user_package=get_package(current_user.package_id).get_json(),
        classes=get_all_classes_json(),
        user_classes=user_classes
    )
    
    
@profile_views.route('/profile/add-class', methods=['POST'])
@login_required
def add_user_class():
    user_classes = [i.get_json() for i in get_userclasses_by_user_id(current_user.id)]
    if request.form['class-name'] in " ".join([i['class_name'] for i in user_classes]):
        flash('User already in class', category='error')
        return redirect(url_for('profile_views.edit_classes_page'))
    
    if create_userclass(current_user.id, request.form['class-id'], request.form['class-name'], False):
        flash('Class added successfully', category='success')
        
    else:
        flash('Unable to add class. Please try again', category='error')
        
    return redirect(url_for('profile_views.edit_classes_page'))


@profile_views.route('/profile/add-class-fitcoin', methods=['POST'])
def add_user_class_fitcoin():
    user_classes = [i.get_json() for i in get_userclasses_by_user_id(current_user.id)]
    if request.form['class-name'] in " ".join([i['class_name'] for i in user_classes]):
        flash('User already in class', category='error')
        return redirect(url_for('profile_views.edit_classes_page'))
    
    if create_userclass(current_user.id, request.form['class-id'], request.form['class-name'], True):
        add_credit(
            wallet_id=current_user.wallet_id,
            credit=int(request.form['class-price'])
        )
        create_transaction(
            user_id=current_user.id,
            wallet_id=current_user.wallet_id,
            type='Credit',
            amount=request.form['class-price'],
            details=f'Sign up fee for {request.form["class-name"]} class',
            datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        flash('Class added successfully', category='success')
        
    else:
        flash('Unable to add class. Please try again', category='error')
        
    return redirect(url_for('profile_views.edit_classes_page'))

@profile_views.route('/profile/remove-class', methods=['POST'])
@login_required
def remove_user_class():
    if get_userclass(current_user.id, request.form['class-id']).paid_by_fitcoin:
        add_debit(
            wallet_id=current_user.wallet_id,
            debit=int(request.form['class-price'])
        )
        create_transaction(
            user_id=current_user.id,
            wallet_id=current_user.wallet_id,
            type='Debit',
            amount=request.form['class-price'],
            details=f'Reimbursement of sign up fee for dropping {request.form["class-name"]} class',
            datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        
    delete_userclass(current_user.id, request.form['class-id'])
    flash('Class removed successfully', category='success')
    return redirect(url_for('profile_views.edit_classes_page'))

    
@profile_views.route('/profile/update-user', methods=['POST'])
@login_required
def update_user_info():
        
    try:
        if request.form['password'] is not None and request.form['password-repeat'] is not None:
            if request.form['password'] != request.form['password-repeat']:
                flash('Passwords do not match', category='error')
                return redirect(url_for('profile_views.profile_page'))
        
        if request.form['username'] != current_user.username:
            if username_exists(request.form['username']):
                flash('Username already exists', category='error')
                return redirect(url_for('profile_views.profile_page'))
        
        dob = date(
            year=int(request.form['dob'].split('-')[0]), 
            month=int(request.form['dob'].split('-')[1]), 
            day=int(request.form['dob'].split('-')[2])
        )
        
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
        curr_user.username=request.form['username']
        curr_user.fname=request.form['firstname']
        curr_user.lname=request.form['lastname']
        curr_user.dob=dob
        curr_user.address=request.form['address']
        curr_user.phone=request.form['contactno']
        curr_user.sex=request.form['sex']
        curr_user.email=request.form['email']
        curr_user.image=image
        curr_user.package_id=request.form['package-id']
        curr_user.set_password(request.form['password'])
        
        # Update emergency contact information
        emergency_contact.fname=em_contact_fname
        emergency_contact.lname=em_contact_lname
        emergency_contact.relation=en_contact_relationship
        emergency_contact.contact=em_contact_contact

        update_user_data(current_user.id, curr_user)
        flash('Profile updated', category='info')
        
    except Exception as e:
        flash("Unable to update profile", category='error')
        
    finally:
        return redirect(url_for('profile_views.edit_profile_page'))