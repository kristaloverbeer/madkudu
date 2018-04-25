import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, DateTime

db: SQLAlchemy = SQLAlchemy()


class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(String, nullable=False)
    name = db.Column(String, nullable=False)
    timestamp = db.Column(DateTime, default=datetime.datetime.utcnow)
