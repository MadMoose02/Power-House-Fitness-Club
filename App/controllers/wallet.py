from App.models import Wallet
from App.database import db


def create_wallet(debit, credit) -> Wallet:
    new_wallet = Wallet(debit=debit, credit=credit)
    db.session.add(new_wallet)
    db.session.commit()
    return new_wallet


def get_wallet(id) -> Wallet:
    return Wallet.query.get(id)


def get_wallet_balance_by_id(id) -> int:
    return Wallet.query.get(id).balance


def add_debit(wallet_id, debit) -> Wallet:
    wallet = Wallet.query.get(wallet_id)
    wallet.debit += debit
    wallet.balance = wallet.debit - wallet.credit
    db.session.add(wallet)
    db.session.commit()
    return wallet


def add_credit(wallet_id, credit) -> Wallet:
    wallet = Wallet.query.get(wallet_id)
    wallet.credit += credit
    wallet.balance = wallet.debit - wallet.credit
    db.session.add(wallet)
    db.session.commit()
    return wallet


def subtract_debit(wallet_id, debit) -> Wallet:
    wallet = Wallet.query.get(wallet_id)
    wallet.debit -= debit
    wallet.balance = wallet.debit - wallet.credit
    db.session.add(wallet)
    db.session.commit()
    return wallet


def subtract_credit(wallet_id, credit) -> Wallet:
    wallet = Wallet.query.get(wallet_id)
    wallet.credit -= credit
    wallet.balance = wallet.debit - wallet.credit
    db.session.add(wallet)
    db.session.commit()
    return wallet