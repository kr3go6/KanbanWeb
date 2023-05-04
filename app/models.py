from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50), nullable=False)
    kanbans = db.relationship('Kanban')

    def __repr__(self):
        return f"user: {self.nickname}"


class Kanban(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"kanban: id = {self.id},\n\
                 uid = {self.uid}\n\
                 type = {self.type}\n"
