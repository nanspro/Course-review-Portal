from flask import Blueprint, request, render_template, \
					flash, g, session, redirect, url_for
from app import db
from app.courses.professors.models import Course
from app.response.models import DisplayForm
from app.form.models import Form
# from app.professors.rating.models import Rating
import pygal
mod_rating = Blueprint('rating', __name__, url_prefix='/faculty/home/rating')

@mod_rating.route('', methods=['POST','GET'])
def get_all_faculty():
	if request.method=="POST":
		profname=session['username']
		courses=Course.query.filter(Course.profname==profname).all()
		selectcourse=request.form.get('select1')
		print(selectcourse)
		lis=[x for x in range(1,11)]
		responses=DisplayForm.query.filter(DisplayForm.courseid==selectcourse).all()
		print(responses)
		resp=[]
		repof=[]
		repo2f=[]
		if selectcourse:
			if responses is not None:
				count=0
				graph1=pygal.Dot()
				graph1.title='% Course Rating'
				graph1.x_labels=lis
				for i in responses:
					print("i is")
					print(i)
					count=count+1
					selected=i.ans
					selected2=i.subj
					resp=selected.split(',')
					resp2=selected2.split('&(a!3')
					repo=[]
					repo2=[]
					for j in resp:
						repo.append(ord(j)-48)
					for j in resp2:
						repo2.append(j)	
					print(repo)
					print(repo2)
					print(resp)
					repof=repo
					repo2f=repo2
					print(resp2)
					graph1.add(str("response"+str(count)),repo)
				graph_data1=graph1.render_data_uri()
				
		questions=Form.query.filter(Form.courseid==selectcourse).first()
		q=''
		q2=''
		repo=[]
		if questions is not None:
			q=questions.questions
			q2=questions.sub	
		ques=[]
		ques2=[]
		if q:
			print(q)
			ques=q.split(',')
			print(ques)
		if q2:
			print(q2)
			ques2=q2.split(',')
			print(ques2)
		selectresponse2=request.form.get('select2')
		resp=[]
		repo=[]
		repo2=[]
		if selectresponse2:
			
			print(selectresponse2)
			selponse=DisplayForm.query.filter(DisplayForm.subj==selectresponse2).first()
			selectresponse=selponse.ans
			print(selectresponse)
			resp=selectresponse.split(',')
			repo2=selectresponse2.split('&(a!3')
			for i in resp:
				repo.append(ord(i)-48)
			print(repo)
			print(repo2)
			graph=pygal.Bar()
			graph.title='% Score'
			graph.x_labels=lis
			graph.add(str(selectcourse),repo)
			graph_data=graph.render_data_uri()
			return render_template("/professors/rating.html",
				courses=courses,responses=responses,
				questions=ques,questions2=ques2,selectresponse=repo,
				selectresponse2=repo2,selectcourse=selectcourse,
				graph_data=graph_data,graph_data1=graph_data1)
		if selectcourse and responses is not None:
			return render_template("/professors/rating.html",
				courses=courses,questions2=ques2,responses=responses,
				questions=ques,selectresponse=repo,selectresponse2=repo2
				,selectcourse=selectcourse,graph_data1=graph_data1)

		return render_template("/professors/rating.html",
			courses=courses,questions2=ques2,responses=responses,
			questions=ques,selectresponse=repo,selectresponse2=repo2
			,selectcourse=selectcourse)
