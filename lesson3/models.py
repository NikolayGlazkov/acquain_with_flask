from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Faculties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facult_name = db.Column(db.String(80), nullable=False)
    students = db.relationship("Student", backref="fakultet", lazy=True)

    def __repr__(self):
        return f"Faculties({self.facult_name})"

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    group = db.Column(db.String(10), nullable=False)
    fakult_id = db.Column(db.Integer, db.ForeignKey("faculties.id"), nullable=False)  # Исправлено здесь

    def __repr__(self):
        return f"Student({self.first_name}, {self.surname}, {self.gender})"

