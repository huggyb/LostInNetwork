# -*- coding: utf-8 -*-

from app import db


class Lan(db.Model):
    """
    Represents a Lan
    """
    friendly_name = "Lan"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    devices = db.relationship('Device', backref='lan', lazy='dynamic')

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return False
        return True

    def __repr__(self):
        return self.name
