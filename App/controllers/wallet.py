from App.models import Wallet
from App.database import db


def create_wallet(user_id, debit, credit) -> Wallet:
    new_wallet = Wallet(user_id=user_id, debit=debit, credit=credit)
    db.session.add(new_wallet)
    db.session.commit()
    return new_wallet