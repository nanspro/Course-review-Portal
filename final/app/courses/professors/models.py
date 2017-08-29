from flask_sqlalchemy import SQLAlchemy
from app import db

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    courseid=db.Column(db.String(20))
    profname=db.Column(db.String(30))
    
    def __init__(self, name, courseid,profname):
        self.name = name
        self.courseid = courseid  
        self.profname=profname
    
    def __repr__(self):
        return "Course { name: %r, Course_id: %r,prof: %r }"%(self.name, self.courseid,self.profname)

db.create_all()
