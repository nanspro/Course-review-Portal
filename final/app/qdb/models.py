from flask_sqlalchemy import SQLAlchemy
from app import db
from flask import *
from sqlalchemy import *

class Questions_1(db.Model):
    __tablename__ = 'questions_t1'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qno = db.Column(db.Integer,unique=True)
    question_t1 = db.Column(db.String(500),unique=True)
    def __init__(self,qno, question_t1):
        self.qno=qno
        self.question_t1 = question_t1
    def __repr__(self):
        return '<question %r>' % self.question_t1
class Questions_2(db.Model):
    __tablename__ = 'questions_t2'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qno = db.Column(db.Integer,unique=True)
    question_t2 = db.Column(db.String(500),unique=True)
    def __init__(self,qno, question_t2):
        self.qno=qno
        self.question_t2 = question_t2
    def __repr__(self):
        return '<question %r>' % self.question_t2       
db.create_all()
