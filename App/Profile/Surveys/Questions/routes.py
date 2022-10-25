from flask import request,redirect,url_for
from flask_login import login_required, current_user,login_user,logout_user
from . import questionsBP 
from .controller import createNewQuestion
from Commons.db import getDB

from .controller import *

# ----------------------------- PROFILE QUESTION --------------------------------------
@questionsBP.route('/new', methods=['GET', 'POST'])
def newQuestion():
    data=request.get_json()
    return createNewQuestion(data)



@questionsBP.route('/')
def indexUsers():
    return "INDEX USER"

