from flask import request
from . import answersBP
from .controller import createNewAnswer
from Commons.db import getDB

from .controller import *

# ----------------------------- PROFILE QUESTION --------------------------------------
@answersBP.route('/new', methods=['GET', 'POST'])
def newQuestion():
    data=request.get_json()
    return createNewAnswer(data)



@answersBP.route('/')
def indexUsers():
    return "INDEX USER"

