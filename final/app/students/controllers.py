from flask import Blueprint, request, render_template, \
				Flask,flash, g, session, redirect, url_for
from app import db
from app.students.models import Student
from app.professors.models import Faculty
from app.students.models import RegistrationForm
from app.courses.students.models import Response
from app.courses.professors.models import Course
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
import re
app =Flask(__name__)
app.config.from_object(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'iiithyd3434@gmail.com'
app.config['MAIL_PASSWORD'] = 'coursereview'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

mod_students = Blueprint('students', __name__, url_prefix='/students')

def is_name(name):
	if re.match("^[A-z]+$", name):
		return True
	return False
def is_roll(roll):
	if re.match("^[0-9]+$", roll):
		return True
	return False	
@mod_students.route('/', methods=['POST','GET'])
def get_all_students():
	form=RegistrationForm()
	return render_template('students/signup.html',form=form)

@mod_students.route('/signup',methods=['POST','GET'])
def result():
	if request.method=='POST':
		form=RegistrationForm(request.form)
		# rollno=request.form.get('roll')
		name=form.username.data
		rollno=form.rollno.data
		print(name)
		# email=request.form.get('email')
		email=form.email.data
		# password=request.form.get('passwd')
		password=form.password.data
		st1=Student.query.filter(Student.email==email).first()
		st2=Student.query.filter(Student.rollno==rollno).first()
		if st2 is not None:
			students= Student.query.all()
			error='This Roll number is already registered'
			return render_template("students/signup.html",students=students,error=error,form=form)
		pro1=Faculty.query.filter(Faculty.email==email).first()
		if st1 is None and pro1 is None :
			msg=Message('Registration',sender='iiithyd3434@gmail.com',recipients=[email])
			msg.body="You have been successfully registered"
			mail.send(msg)
			if form.validate() and is_name(name):
				u = Student(name,rollno,email,password)
				db.session.add(u) 
				db.session.commit()
				form.username.data=None
				form.rollno.data=None
				form.email.data=None
			if not is_name(name):
				students= Student.query.all()
			# 	form.username.data=None
			# form.rollno.data=None
			# form.email.data=None
				error='Name must contain only alphabets'
				return render_template("students/signup.html",students=students,error=error,form=form)
			if not is_roll(rollno):
				students= Student.query.all()
			# 	form.username.data=None
			# form.rollno.data=None
			# form.email.data=None
				error='Rollno must contain only numbers'
				return render_template("students/signup.html",students=students,error=error,form=form)	
			students= Student.query.all()
			return render_template("students/signup.html",students=students,form=form)
		if st1 is not None or pro1 is not None :
			error='This Email id is already registered.'
			form.username.data=None
			form.rollno.data=None
			form.email.data=None	
			students= Student.query.all()
			return render_template("students/signup.html",students=students,error=error,form=form)
@mod_students.route('/home',methods=['POST','GET'])
def res():
	if request.method =='POST':
		email=request.form.get('email')
		password=request.form.get('passwd')
		student=Student.query.filter(Student.email==email).first()
		courses=Course.query.all()
		if student is None or not student.check_password(password):
			form=RegistrationForm(request.form)
			error='Invalid password.'
			form.username.data=None
			form.rollno.data=None
			form.email.data=None
			return render_template('students/signup.html',form=form,error=error)
		else:
			session['username']=student.name
			studname=student.name
			session.permanent = True
			courses=Course.query.all()
			courses3=Response.query.filter(Response.studname==studname).all()
			print(session['username'])
			return render_template('students/home.html',courses=courses,courses3=courses3,name=session['username'])
	else:
		name=session.get('username')
		courses=Course.query.all()
		courses3=Response.query.filter(Response.studname==name).all()
		return render_template('students/home.html',courses=courses,courses3=courses3,name=name)
