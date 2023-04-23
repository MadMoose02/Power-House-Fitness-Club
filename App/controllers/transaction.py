from App.models import Transaction
from App.database import db


def create_transaction(user_id, wallet_id, details, datetime) -> Transaction:
    new_transaction = Transaction(
        user_id=user_id,
        wallet_id=wallet_id,
        details=details,
        datetime=datetime
    )
    db.session.add(new_transaction)
    db.session.commit()
    return new_transaction


def get_transaction(id) -> Transaction:
    return Transaction.query.get(id)