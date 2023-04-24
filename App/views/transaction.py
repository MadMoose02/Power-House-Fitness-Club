from flask import Blueprint, render_template
from flask_login import current_user, login_required

from App.models import db
from App.controllers import get_package, get_all_transactions_of_user_json

transaction_views = Blueprint('transaction_views', __name__, template_folder='../templates')

@transaction_views.route('/transactions', methods=['GET'])
@login_required
def transactions_history_page():
    return render_template(
        'transaction-history.html', 
        user=current_user, 
        user_package=get_package(current_user.package_id).get_json(),
        transactions=get_all_transactions_of_user_json(current_user.id)
    )