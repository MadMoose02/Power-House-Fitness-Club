from datetime import datetime as dt
from App.models import Transaction
from App.database import db


def create_transaction(user_id, wallet_id, type, amount, details, datetime) -> Transaction:
    new_transaction = Transaction(
        user_id=user_id,
        wallet_id=wallet_id,
        type=type,
        amount=amount,
        details=details,
        datetime=datetime
    )
    db.session.add(new_transaction)
    db.session.commit()
    return new_transaction


def get_transaction(id) -> Transaction:
    return Transaction.query.get(id)


def get_all_transactions():
    return Transaction.query.all()


def get_all_transactions_of_user(user_id):
    return Transaction.query.filter_by(user_id=user_id).all()


def get_all_transactions_of_user_json(user_id):
    return [i.get_json() for i in get_all_transactions_of_user(user_id)]