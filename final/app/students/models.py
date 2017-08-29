from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from wtforms import validators, ValidationError
from wtforms import Form, BooleanField, StringField, PasswordField, validators
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    rollno=db.Column(db.String(20))
    email=db.Column(db.String(100))
    password=db.Column(db.String(100))
    def __init__(self, name, rollno, email, password):
        self.name = name
        self.rollno = rollno
        self.email = email
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)

class RegistrationForm(Form):
    username = StringField('Username',[validators.Length(min=4, max=25, message="Username must be betwen 4 & 25 characters")] )
    email = StringField('Email-id', [validators.Length(min=4, max=35, message="E-mail must be betwen 4 & 35 characters")])
    rollno =StringField("rollno",[validators.Length(min=4, max=8,message="Roll must be between 4 to 8 digits")])
    password = PasswordField('Password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('RePassword')
    submit = SubmitField("SignUp")  
    recaptcha = RecaptchaField()      

    def __repr__(self):
        return "Student { name: %r, rollno: %r , email: %r, password: %r }"%(self.name, self.rollno,self.email, self.password)

db.create_all()
