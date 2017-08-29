from flask import Blueprint,Flask,request, render_template, \
				flash, g, session, redirect, url_for
from app import db
from app.courses.students.models import Response
from app.courses.professors.models import Course
app = Flask(__name__)

mod_response = Blueprint('response', __name__, url_prefix='/students/home')

@mod_response.route('/courses', methods=['POST','GET'])
def get_all_courses():
	studname=session['username']
	print("incourses")
	print(studname)
	error=None
	courses=Course.query.all()
	courses3=Response.query.filter(Response.studname==studname).all()
	return render_template('students/courses.html',courses=courses,courses3=courses3,studname=studname,error=error)

@mod_response.route('/courses/change',methods=['POST','GET'])
def result():
	if request.method=='POST':
		courseid=request.form.get('courseid')
		studname=session['username']
		# cours=Response.query.filter(Response.courseid==courseid).first()
		courses3=Response.query.filter(Response.studname==studname).all()
		cours=0
		courseId=request.form.get('select')
		for i in courses3:
			if i.courseid==courseid:
				cours=1

		print("cours")
		if cours ==0 and courseId is None:
			u = Response(courseid,studname)
			db.session.add(u) 
			print(u.studname)
			db.session.commit()
			courses=Course.query.all()
			courses3=Response.query.filter(Response.studname==studname).all()
			# print(courses3)
			print(courses3)
			return render_template("students/courses.html",courses=courses,courses3=courses3,studname=studname)
		if cours ==1 :
			error='This course is already registered.'
			courses=Course.query.all()
			courses3=Response.query.filter(Response.studname==studname).all()
			return render_template("students/courses.html",courses=courses,courses3=courses3,studname=studname,error=error)
		if courseId is not None :
			course=Response.query.filter(Response.courseid==courseId).first()
			db.session.delete(course)
			db.session.commit()
			courses=Course.query.all()
			courses3=Response.query.filter(Response.studname==studname).all()
			print(courses3)
			return render_template("students/courses.html",courses=courses,courses3=courses3,studname=studname)

	else:
		courses=Course.query.all()
		courses3=Response.query.filter(Response.studname==studname).all()
		return render_template("students/courses.html",courses=courses,courses3=courses3,studname=studname)
