from datetime import date, datetime
from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import current_user, login_required

from App.models import db
from App.controllers import (
    retrieve_current_user, 
    get_package, 
    create_activity, 
    add_debit,
    get_all_activities_of_user_json,
    create_transaction
)

activity_views = Blueprint('activity_views', __name__, template_folder='../templates')

@activity_views.route('/log-activity', methods=['GET'])
@login_required
def log_activity_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    user_package = get_package(user.package_id).get_json() if user else None
    return render_template('log-activity.html', user=user, user_package=user_package)


@activity_views.route('/log-activity', methods=['POST'])
@login_required
def add_activity_log():
    print(request.form.to_dict())
    debit_points = 10
    if create_activity(
        user_id=current_user.id,
        date=date(
            year=int(request.form['date'].split('-')[0]), 
            month=int(request.form['date'].split('-')[1]), 
            day=int(request.form['date'].split('-')[2])
        ),
        pre_workout=bool(request.form['pre-workout']),
        energy_level=request.form['energy-level'],
        details=request.form['details'],
    ):
        # Add fitcoins to the user's wallet
        add_debit(wallet_id=current_user.wallet_id, debit=debit_points)
        dt = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        create_transaction(
            user_id=current_user.id, 
            wallet_id=current_user.wallet_id, 
            type="Debit",
            amount=debit_points,
            details="Added 10 fitcoins to debit for completing an activity",
            datetime=dt
        )
        flash("Activity successfully logged. Fitcoins added to wallet", category='success')
    else:
        flash("Something went wrong whilst logging your activity. Try again", category='error')
        db.session.rollback()
        
    return redirect(url_for('activity_views.log_activity_page'))


@activity_views.route('/activty-tracking', methods=['GET'])
@login_required
def activty_tracking_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    user_package = get_package(user.package_id).get_json() if user else None
    return render_template(
        'activtiy-tracking.html', 
        user=user, 
        user_package=user_package,
        activities = get_all_activities_of_user_json(current_user.id)
    )