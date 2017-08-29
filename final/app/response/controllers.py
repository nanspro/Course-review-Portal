from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.form.models import Form
from app.response.models import DisplayForm
from app.courses.students.models import Response
from app.qdb.models import Questions_2
from app.courses.professors.models import Course

mod_displayform = Blueprint('displayform', __name__, url_prefix='/students/home')

@mod_displayform.route('/form',methods=['POST','GET'])
def open():
    studname=session.get('username')
    course=request.form.get('select')
    form = Form.query.filter(course==Form.courseid).first()
    if form is None:
        error="Form of this course has not been made"
        return render_template("/students/submit.html",Course=course,studname=studname,error=error)
    else :
        questions=(form.questions).split(',')
        sub=(form.sub).split(',')
        return render_template("/students/submit.html",Course=course,questions=questions,studname=studname,sub=sub)


@mod_displayform.route('/form/final',methods=['POST','GET'])
def ope1n():
    ans=request.form.getlist('checks')
    ans2=request.form.getlist('Text')
    course=request.form.get('select')
    cours=DisplayForm.query.filter(DisplayForm.courseid==course).first()
    if cours is None :
        print(ans)
        string=""
        for i in ans:
            if len(string) ==0:
                string=i
            else:
                string=string+','+i
        answer=string
        string2=""
        for i in ans2:
            if len(string2) ==0:
                string2=i
            else:
                string2=string2+'&(a!3'+i
        answer2=string2
        studname=request.form.get('studname')
        print(answer)
        print(studname)
        anslist=DisplayForm(course,answer,studname,answer2)
        db.session.add(anslist)
        db.session.commit()
        return render_template("students/final.html")
    else :
        db.session.delete(cours)
        error='Review for the course is Updated.'
        ans=request.form.getlist('checks')
    ans2=request.form.getlist('Text')
    course=request.form.get('select')
    cours=DisplayForm.query.filter(DisplayForm.courseid==course).first()
    if cours is None :
        print(ans)
        string=""
        for i in ans:
            if len(string) ==0:
                string=i
            else:
                string=string+','+i
        answer=string
        string2=""
        for i in ans2:
            if len(string2) ==0:
                string2=i
            else:
                string2=string2+'&(a!3'+i
        answer2=string2
        studname=request.form.get('studname')
        print(answer)
        print(studname)
        anslist=DisplayForm(course,answer,studname,answer2)
        db.session.add(anslist)
        db.session.commit()
        return render_template("students/final.html",error=error)
        # courses=Course.query.all()
        # studname=session.get('username')
        # courses3=Response.query.filter(Response.studname==studname).all()
        # # print(session['username'])
        # error='Response for this is already submitted.Try for other course.'
        # return render_template('students/home.html',error=error,courses=courses,courses3=courses3,name=)