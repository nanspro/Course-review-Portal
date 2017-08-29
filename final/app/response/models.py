from flask_sqlalchemy import SQLAlchemy
from app import db

class DisplayForm(db.Model):
    __tablename__ = 'displayform'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courseid = db.Column(db.String(30))
    studname = db.Column(db.String(30))
    ans = db.Column(db.String(5000))
    subj = db.Column(db.String(50000))
    def __init__(self,courseid, ans,studname,subj):
        self.courseid=courseid
        self.studname=studname
        self.ans = ans
        self.subj = subj
    def __repr__(self):
        return '<question %r %r>' % (self.ans,self.subj)
db.create_all()
