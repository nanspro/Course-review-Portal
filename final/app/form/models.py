from flask_sqlalchemy import SQLAlchemy
from app import db

class Form(db.Model):
    __tablename__ = 'form'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courseid = db.Column(db.String(30))
    questions = db.Column(db.String(5000))
    sub = db.Column(db.String(5000))
    def __init__(self,courseid, questions ,sub):
        self.courseid=courseid
        self.questions = questions
        self.sub = sub
    def __repr__(self):
        return '<question %r>' % self.questions
db.create_all()
