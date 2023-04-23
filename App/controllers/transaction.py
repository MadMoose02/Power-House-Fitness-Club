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


def get_all_transactions() -> list[Transaction]:
    return Transaction.query.all()