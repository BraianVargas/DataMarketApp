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

@answersBP.route('/get', methods=['GET', 'POST'])
def getanswers():
    db, c = getDB()
    q = "SELECT * FROM profileanswer"
    c.execute(q)
    a = c.fetchall()
    return a



@answersBP.route('/')
def indexUsers():
    return "INDEX USER"

