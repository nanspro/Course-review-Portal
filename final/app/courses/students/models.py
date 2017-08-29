from flask_sqlalchemy import SQLAlchemy
from app import db
class Response(db.Model):
	__tablename__ = 'response'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	courseid=db.Column(db.String(20))
	studname=db.Column(db.String(30))

	def __init__(self, courseid,studname):
		self.courseid = courseid 
		self.studname=studname

	def __repr__(self):
		return "Response { Course_id: %r, Student_name= %r }"%(self.courseid,self.studname)

db.create_all()
