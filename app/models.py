from flask_login import UserMixin
from app import db


class UserModel(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)

    def __str__(self):
        return f'{self.id}) {self.email}'

    def __repr__(self):
        return f'{self.id}) {self.email}'

class PetModel(db.Model):
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    animal_type = db.Column(db.String(20), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    def __str__(self):
        return f'{self.id}) {self.name}'

    def __repr__(self):
        return f'{self.id}) {self.name}'


class OwnerModel(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(20), nullable=False)
    pets = db.relationship('PetModel', backref='owner', cascade='all, delete', lazy=True)

    def __str__(self):
        return f'{self.id}) {self.name}'

    def __repr__(self):
        return f'{self.id}) {self.name}'