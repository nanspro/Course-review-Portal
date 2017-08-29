from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.form.models import Form
from app.qdb.models import Questions_2
from app.qdb.models import Questions_1
from app.courses.professors.models import Course

mod_form = Blueprint('form', __name__, url_prefix='/faculty/home/form')

@mod_form.route('',methods=['POST','GET'])
def open():
	q=Questions_2.query.all()
	q2=Questions_1.query.all()
	courses=Course.query.all()
	profname=session['username']
	print("in form")
	print(profname)
	courses1= Course.query.filter(Course.profname==profname).all()
	return render_template("questions/table.html",q=q,q2=q2,profname=profname,courses=courses1)

@mod_form.route('/make',methods=['POST','GET'])
def mac():
	if request.method=='POST':
		courseId=request.form.get('select1')
		error='Form is made for the course.'
		cours=Form.query.filter(Form.courseid==courseId).first()
		if cours is None :
			test = request.form.getlist('checks')
			test2 = request.form.getlist('checks2')
			print("test")
			print(test)
			print("test2")
			print(test2)
			stri=""
			for i in test:
				if len(stri) == 0:
					stri = i
				else :
					stri = stri +','+i	
			best = stri
			alla = best.split(',')
			stri2=""
			for i in test2:
				if len(stri2) == 0:
					stri2 = i
				else :
					stri2 = stri2 +','+i	
			best2 = stri2
			print(best2)
			alla2 = best2.split(',')
			u = Form(courseId,best,best2)
			db.session.add(u)
			db.session.commit() 
			forms= Form.query.all()
			return render_template("professors/final.html",test=alla,test2=alla2,course=courseId,error=error)
		else :
			db.session.delete(cours)
			error='Form for the course is Updated.'
			q=Questions_2.query.all()
			courses=Course.query.all()
			profname=session['username']
			courses1= Course.query.filter(Course.profname==profname).all()
			test = request.form.getlist('checks')
			test2 = request.form.getlist('checks2')
			print("test")
			print(test)
			print("test2")
			print(test2)
			stri=""
			for i in test:
				if len(stri) == 0:
					stri = i
				else :
					stri = stri +','+i	
			best = stri
			alla = best.split(',')
			stri2=""
			for i in test2:
				if len(stri2) == 0:
					stri2 = i
				else :
					stri2 = stri2 +'&(a!3'+i	
			best2 = stri2
			print(best2)
			alla2 = best2.split('&(a!3')
			u = Form(courseId,best,best2)
			db.session.add(u)
			db.session.commit() 
			forms= Form.query.all()
			return render_template("professors/final.html",test=alla,test2=alla2,course=courseId,error=error)
			# return render_template("questions/table.html",q=q,profname=profname,courses=courses1,error=error)


