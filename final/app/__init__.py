# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
from flask_mail import Mail, Message
mail=Mail(app)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.students.controllers import mod_students
from app.root.controllers import mod_root
from app.qdb.controllers import mod_qdb
from app.professors.controllers import mod_faculty
from app.courses.professors.controllers import mod_professor
from app.form.controllers import mod_form
from app.courses.students.controllers import mod_response
from app.response.controllers import mod_displayform
from app.professors.rating.controllers import mod_rating


# Register blueprint(s)
app.register_blueprint(mod_students)
app.register_blueprint(mod_root)
app.register_blueprint(mod_qdb)
app.register_blueprint(mod_faculty)
app.register_blueprint(mod_professor)
app.register_blueprint(mod_form)
app.register_blueprint(mod_response)
app.register_blueprint(mod_displayform)
app.register_blueprint(mod_rating)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
