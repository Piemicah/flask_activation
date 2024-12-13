from config import db
from datetime import datetime, timezone


class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activation_key = db.Column(db.String(100), unique=True)
    account = db.Column(db.String(40), unique=True, nullable=True)
    created_at = db.Column(db.String(80), nullable=True)

    def to_json(self):
        return {
            "key": self.activation_key,
            "account": self.account,
            "created": self.created_at,
        }
