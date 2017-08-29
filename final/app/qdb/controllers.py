from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.qdb.models import Questions_2
mod_qdb = Blueprint('qdb', __name__, url_prefix='/questions')


@mod_qdb.route('/all',methods=['POST','GET'])
def result():
    q=Questions_2.query.all()
    q2=Questions_1.query.all()
    return render_template("questions/table.html",q=q,q2=q2)
