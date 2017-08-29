from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
#from app.students.models import Student

mod_root = Blueprint('root', __name__)

@mod_root.route('/', methods=['GET'])
def get():
    return render_template('index.html')
