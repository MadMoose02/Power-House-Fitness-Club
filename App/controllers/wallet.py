from App.models import Wallet
from App.database import db


def create_wallet(user_id, debit, credit) -> Wallet:
    new_wallet = Wallet(user_id=user_id, debit=debit, credit=credit)
    db.session.add(new_wallet)
    db.session.commit()
    return new_wallet


def get_wallet(id) -> Wallet:
    return Wallet.query.get(id)


def add_debit(wallet_id, debit) -> Wallet:
    wallet = Wallet.query.get(wallet_id)
    wallet.debit += debit
    db.session.add(wallet)
    db.session.commit()
    return wallet


def add_credit(wallet_id, credit) -> Wallet:
    wallet = Wallet.query.get(wallet_id)
    wallet.credit += credit
    db.session.add(wallet)
    db.session.commit()
    return wallet


def subtract_debit(wallet_id, debit) -> Wallet:
    wallet = Wallet.query.get(wallet_id)
    wallet.debit -= debit
    db.session.add(wallet)
    db.session.commit()
    return wallet


def subtract_credit(wallet_id, credit) -> Wallet:
    wallet = Wallet.query.get(wallet_id)
    wallet.credit -= credit
    db.session.add(wallet)
    db.session.commit()
    return wallet