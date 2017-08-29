from flask import *
from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class Questions_1(db.Model):
    __tablename__ = 'questions_t1'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qno = db.Column(db.Integer)
    question_t1 = db.Column(db.String(500),unique=True)
    def __init__(self, qno,question_t1):
        self.qno=qno
        self.question_t1 = question_t1
    def __repr__(self):
        return '<question %r>' % self.question_t1
class Questions_2(db.Model):
    __tablename__ = 'questions_t2'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qno = db.Column(db.Integer)
    question_t2 = db.Column(db.String(500),unique=True)
    def __init__(self, qno,question_t2):
        self.qno=qno
        self.question_t2 = question_t2
    def __repr__(self):
        return '<question %r>' % self.question_t2
        
db.create_all()
sub1 = Questions_1(1,'Write your views about the course.')
sub2 = Questions_1(2,'Write your views about the faculty.')
sub3 = Questions_1(3,'Sugession for improvising course .')
sub4 = Questions_1(4,'Any other point you would like to mention .')
sub5 = Questions_1(5,'Any experience would like to share .')
Question1 = Questions_2(1,'clearly identifies expectations at the begining of the course')
Question2 = Questions_2(2,'follows course syllabus or outline strictly ')
Question3 = Questions_2(3,'uses example and rephrases concepts ideas and explanation ') 
Question4 = Questions_2(4,'meets and dismisses class on time')
Question5 = Questions_2(5,'provides accessibility (keeps office hours)')
Question6 = Questions_2(6,'uses class time effectively ')
Question7 = Questions_2(7,'responds to voice mails & emails')
Question8 = Questions_2(8,'explains course content successfully')
Question9 = Questions_2(9,'uses examples and rephrases concepts & ideas and explanation') 
Question10 = Questions_2(10,'covers course material on exam')
Question11 = Questions_2(11,'encourages an atmosphere of mutual respect and courtesy') 
Question12 = Questions_2(12,'provides constructive feedback (gives suggestion for improvement etc')
Question13 = Questions_2(13,'communicates effectively (is enthusastic about the subject and speaks clearly)')
Question14 = Questions_2(14,'encourages an atmosphere of mutual respect and courtsey') 
Question15 = Questions_2(15,'provides an opurtunity to work efficiently overall')
Question16 = Questions_2(16,'encourages student to form study groups outside of class')
Question17 = Questions_2(17,'encourages to contribute to class discussion')
Question18 = Questions_2(18,'expects a high level of academic performance')
Question19 = Questions_2(19,'utilizes educational resources effectively(i.e. media ppt)')
Question20 = Questions_2(20,'utilizes of appropriate instructional techniques (demonstrations case studeies etc)')
db.session.add(sub1)
db.session.add(sub2)
db.session.add(sub3)
db.session.add(sub4)
db.session.add(sub5)
db.session.add(Question1)
db.session.add(Question2)
db.session.add(Question3)
db.session.add(Question4)
db.session.add(Question5)
db.session.add(Question6)
db.session.add(Question7)
db.session.add(Question8)
db.session.add(Question9)
db.session.add(Question10)
db.session.add(Question11)
db.session.add(Question12)
db.session.add(Question13)
db.session.add(Question14)
db.session.add(Question15)
db.session.add(Question16)
db.session.add(Question17)
db.session.add(Question18)
db.session.add(Question19)
db.session.add(Question20)
db.session.commit()
