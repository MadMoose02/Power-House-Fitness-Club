from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import current_user, login_required

from App.models import db, Wallet
from App.controllers import get_wallet, get_package, get_all_transactions_of_user_json

wallet_views = Blueprint('wallet_views', __name__, template_folder='../templates')

@wallet_views.route('/wallet', methods=['GET'])
@login_required
def wallet_page():
    user_package = get_package(current_user.package_id).get_json()
    transactions = get_all_transactions_of_user_json(current_user.id)
    return render_template(
        'wallet.html', 
        user=current_user, 
        user_package=user_package, 
        wallet=get_wallet(current_user), 
        transactions=transactions
    )
