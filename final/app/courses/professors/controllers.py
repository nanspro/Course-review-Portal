from flask import Blueprint,Flask,request, render_template, \
				flash, g, session, redirect, url_for
from app import db
from app.courses.professors.models import Course
from app.courses.students.models import Response
from app.form.models import Form
from app.response.models import DisplayForm
import re
app = Flask(__name__)

mod_professor = Blueprint('professor', __name__, url_prefix='/faculty/home')

def is_name(name):
	if re.match("^[A-z]+$", name):
		return True
	return False
@mod_professor.route('/courses', methods=['POST','GET'])
def get_all_courses():
	profname=session['username']
	courses=Course.query.filter(Course.profname==profname).all()
	return render_template('professors/courses.html',courses=courses)

@mod_professor.route('/courses/change',methods=['POST','GET'])
def result():
	if request.method=='POST':
		name=request.form.get('name')
		print("name")
		print(name)
		courseid=request.form.get('courseid')
		cours=Course.query.filter(Course.courseid==courseid).first()
		profname=session['username']
		print(cours)
		courseId=request.form.get('select')
		if courseId is not None :
			course=Course.query.filter(Course.courseid==courseId).first()
			db.session.delete(course)
			responses=Response.query.filter(Response.courseid==courseId).all()
			for i in responses:
				db.session.delete(i)
			form=Form.query.filter(Form.courseid==courseId).first()
			if form is not None:
				db.session.delete(form)
			ans=DisplayForm.query.filter(DisplayForm.courseid==courseId).all()
			for i in ans:
				db.session.delete(i)
			db.session.commit()
			courses=Course.query.all()
			courses1= Course.query.filter(Course.profname==profname).all()
			print(courses1)
			return render_template("professors/courses.html",courses=courses1)
		if cours is None and len(name) != 0 and len(courseid) !=0:
			u = Course(name,courseid,profname)
			print('u')
			print(u)
			error=None
			profname=session['username']
			if is_name(name):
				db.session.add(u) 
				print(u.profname)
				db.session.commit()
			else:
				error='Course name should have only alphabets'
			courses=Course.query.all()
			courses1= Course.query.filter(Course.profname==profname).all()
			print(courses1)
			return render_template("professors/courses.html",courses=courses1,error=error)
		if cours is not None :
			error='This course is already registered.'
			print(error)
			courses1= Course.query.filter(Course.profname==profname).all()
			return render_template("professors/courses.html",courses=courses1,error=error)
		if len(name) == 0 :
			error='coursename is empty.'
			print(error)
			courses1= Course.query.filter(Course.profname==profname).all()
			return render_template("professors/courses.html",courses=courses1,error=error)
		if len(courseid) ==0 :
			error='courseid is empty.'
			print(error)
			courses1= Course.query.filter(Course.profname==profname).all()
			return render_template("professors/courses.html",courses=courses1,error=error)			
	else:
		return render_template("professors/courses.html",courses=courses1)
