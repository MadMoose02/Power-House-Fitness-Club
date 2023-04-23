from datetime import datetime
from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import current_user, login_required

from App.models import db
from App.controllers import (
    retrieve_current_user, 
    get_package, 
    create_discussion,
    create_message,
    get_discussion,
    get_discussions_by_title, 
    get_all_discussions,
    get_messages_by_discussion,
    get_user
)

discussion_views = Blueprint('discussion_views', __name__, template_folder='../templates')

@discussion_views.route('/forum', methods=['GET'])
def forum_page():
    user = retrieve_current_user() if current_user.is_authenticated else None
    user_package = get_package(user.package_id).get_json() if user else None
    discussions = get_all_discussions()
    return render_template(
        'forum.html', 
        user=user, 
        user_package=user_package, 
        discussions=get_all_discussions(),
        get_user=get_user
    )


@discussion_views.route('/start-discussion', methods=['POST'])
def start_new_discussion():
    if not current_user.is_authenticated:
        flash('You must be logged in to create a discussion')
        return redirect(url_for('discussion_views.forum_page'))
    
    if get_discussions_by_title(request.form['title']):
        flash('Discussion with that title already exists!', category='error')
        return redirect(url_for('discussion_views.forum_page'))
    
    if create_discussion(request.form['title'], current_user.id):
        flash('Discussion created successfully', category='success')
    else:
        flash('Unable to create discussion. Please try again', category='error')    
        
    return redirect(url_for('discussion_views.forum_page'))


@discussion_views.route('/forum/<int:discussion_id>', methods=['GET'])
def view_discussion(discussion_id: int):
    user = retrieve_current_user() if current_user.is_authenticated else None
    user_package = get_package(user.package_id).get_json() if user else None
    return render_template(
        'discussion.html', 
        user=user, 
        user_package=user_package,
        get_user=get_user,
        discussion=get_discussion(discussion_id),
        messages=get_messages_by_discussion(discussion_id)
    )
    
    
@discussion_views.route('/forum/<int:discussion_id>/create-message', methods=['POST'])
def create_new_message(discussion_id: int):
    if not current_user.is_authenticated:
        flash('You must be logged in to create a message')
        return redirect(url_for('discussion_views.view_discussion', discussion_id=discussion_id))
    
    if not get_discussion(discussion_id):
        flash('Discussion does not exist!', category='error')
        return redirect(url_for('discussion_views.view_discussion', discussion_id=discussion_id))
    
    if create_message(discussion_id, current_user.id, request.form['content'], datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
        flash('Message created successfully', category='success')
    else:
        flash('Unable to create message. Please try again', category='error')
    
    return redirect(url_for('discussion_views.view_discussion', discussion_id=discussion_id))