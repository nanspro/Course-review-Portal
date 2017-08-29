from flask import Blueprint, request, render_template, \
					Flask,flash, g, session, redirect, url_for
from app import db
from app.professors.models import Faculty
from app.professors.models import RegistrationForm
from app.students.models import Student
from app.courses.professors.models import Course
from app.courses.students.models import Response
from app.response.models import DisplayForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
import re
import pygal
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

mod_faculty = Blueprint('faculty', __name__, url_prefix='/faculty')

def is_name(name):
	if re.match("^[A-z]+$", name):
		return True
	return False
@mod_faculty.route('/', methods=['POST','GET'])
def get_all_faculty():
	form=RegistrationForm()
	return render_template('professors/signup.html',form=form)

@mod_faculty.route('/all', methods=['GET'])
def get_prof(rollno):
	faculty=Faculty.query.all()
	return render_template('professors/table.html', faculty=faculty)

@mod_faculty.route('/signup',methods=['POST','GET'])
def result():
	if request.method=='POST':
		form=RegistrationForm(request.form)
		# name=request.form.get('name')
		name=form.username.data
		print(name)
		# email=request.form.get('email')
		email=form.email.data
		# password=request.form.get('passwd')
		password=form.password.data
		st1=Student.query.filter(Student.email==email).first()
		pro1=Faculty.query.filter(Faculty.email==email).first()
		if st1 is None and pro1 is None:
			msg=Message('Registration',sender='iiithyd3434@gmail.com',recipients=[email])
			msg.body="You have been successfully registered."
			mail.send(msg)
			if form.validate() and is_name(name):
				u = Faculty(name,email,password)
				db.session.add(u)
				db.session.commit()
				form.username.data=None
				form.email.data=None
			if not is_name(name):
				error='Name must contain only alphabets'
				faculty= Faculty.query.all()
				return render_template("professors/signup.html",faculty=faculty,form=form,error=error)
			faculty= Faculty.query.all()
			return render_template("professors/signup.html",faculty=faculty,form=form)
		if st1 is not None or pro1 is not None :
			error='This Email id is already registered.'
			faculty= Faculty.query.all()
			return render_template("professors/signup.html",faculty=faculty,error=error,form=form)	

@mod_faculty.route('/home',methods=['POST','GET'])
def login():
	lis=[u for u in range(1,3)]
	liss=["courses"]
	if request.method =='POST':
		email=request.form.get('email')
		password=request.form.get('passwd')
		courses=Course.query.all()
		overallrating=0
		faculty=Faculty.query.filter(Faculty.email==email).first()
		if faculty is None or not faculty.check_password(password):
			session.pop('username',None)
			error='This Password is Invalid.'
			form=RegistrationForm(request.form)
			faculty= Faculty.query.all()
			form.email.data=None
			form.username.data=None
			return render_template('professors/signup.html',faculty=faculty,error=error,form=form)
		else:
			print(email)
			print(password)
			session['username']=faculty.name
			name=session['username']
			session.permanent = True
			print(session['username'])
			#prof_courses=Course.query.filter(Course.profname==name).all()
			
			#print(responsecount)
			#print(prof_courses)
			responsecount=0
			prof_courses=Course.query.filter(Course.profname==name).all()
			overallsum=0
			if prof_courses is not None:
				print(prof_courses)
				temp=0
				graph1=pygal.Bar()
				graph1.title='% profcourserating'
				graph1.x_labels=liss
				
				for course in prof_courses:
					courserating=0
					temp=temp+1
					z=course.courseid
					y=DisplayForm.query.filter(DisplayForm.courseid==z).all()
					resp=[]
					print(z)
					print(y)
					
					if len(y)!=0:
						responsecount=responsecount+1
						count=0
						s=0
						for i in y:
							k=0
							selected=i.ans
							resp=selected.split(',')
							repo=[]
							for j in resp:
								repo.append(ord(j)-48)
							print(repo)
							for j in repo:
								k=k+j
							k=k/5
							print(k)
							count=count+1
							s=s+k
							print(s)
						courserating=s/count
						graph1.add(str(course.name),[courserating])
						
						print(courserating)
						overallsum=overallsum+courserating

						if responsecount !=0:
							overallrating=overallsum/responsecount
							print(overallrating)
					#if courserating!=0:
						#graph=pygal.Line()
						#graph.title='% profcourserating'
						#graph.x_labels=liss
						#graph.add(str(course),courserating)
						#graph_data=graph.render_data_uri()
				graph_data1=graph1.render_data_uri()
		if overallrating !=0:

			graph=pygal.Pie()
			graph.title='% prof rating'
			graph.x_labels=lis
			graph.add("rating",overallrating)
			graph.add("10-rating",10-overallrating)
			graph_data=graph.render_data_uri()
			return render_template('professors/home.html',name=name,courses=courses,rating=overallrating,graph_data=graph_data,graph_data1=graph_data1)
		return render_template('professors/home.html',name=name,courses=courses)
	else:
		overallrating=0
		name=session.get('username')
		responsecount=0	
		prof_courses=Course.query.filter(Course.profname==name).all()
		overallsum=0
		if prof_courses is not None:
			liss=["courses"]
			print(prof_courses)
			graph1=pygal.Bar()
			graph1.title='% profcourserating'
			graph1.x_labels=liss
			for course in prof_courses:
				
				z=course.courseid
				y=DisplayForm.query.filter(DisplayForm.courseid==z).all()
				resp=[]
				print(z)
				print(y)
				print(len(y))
				
				if len(y)!=0:
					responsecount=responsecount+1
					count=0
					s=0
					for i in y:
						k=0
						selected=i.ans
						resp=selected.split(',')
						repo=[]
						for j in resp:
							repo.append(ord(j)-48)
						print(repo)
						for j in repo:
							k=k+j
						k=k/5
						print(k)
						count=count+1
						s=s+k
						print(s)
					courserating=s/count
					graph1.add(str(course.name),[courserating])
					print(courserating)
					overallsum=overallsum+courserating
					if responsecount !=0:
						overallrating=overallsum/responsecount
						print(overallrating)
			graph_data1=graph1.render_data_uri()
		if overallrating !=0:
			graph=pygal.Pie()
			graph.title='% prof rating'
			graph.x_labels=lis
			graph.add("rating",overallrating)
			graph.add("10-rating",10-overallrating)
			graph_data=graph.render_data_uri()
			courses=Course.query.all()
			return render_template('professors/home.html',name=name,courses=courses,rating=overallrating,graph_data=graph_data,graph_data1=graph_data1)
		else:

			courses=Course.query.all()
			return render_template('professors/home.html',name=name,courses=courses)
