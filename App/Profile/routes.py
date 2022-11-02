from flask import request,redirect,url_for
from flask_login import login_required, current_user,login_user,logout_user
from App.Profile import profileBP
from Commons.db import getDB

from .controller import *
from .Surveys.Answers import controller as answerController

# ----------------------------- BUSQUEDAS Y FILTROS --------------------------------------
"""
It gets all the users from the database and returns them.
:return: A list of tuples.
""" 
@profileBP.route('/get/all', methods=["GET","POST"])
# @login_required
def getUsers():
    db, c = getDB()
    c.execute("SELECT * FROM profile ORDER BY id ASC")
    users = c.fetchall()

    if users != None:
        return users
    else:
        return "404 - User Table Is Empty"

@profileBP.route("/search", methods=['GET','POST'])
@login_required
def searchUser():
    #Se recibe el argumento como KEY o JSON
    i = get_users(request.get_json())
    return i

@profileBP.route('/new', methods = ["POST"])
# @login_required 
def createProfile():
    data = request.get_json()

    message = createNewProfile(data)

    return message

# ----------------------------- VERIFICACIÓN DE USUARIO --------------------------------------
    """
    It takes a list of objects, each object has a userId, questionId, and answer. It then creates a new
    answer in the database, gets the id of the answer, and then inserts the userId, questionId, and
    answerId into the profileuserdetail table
    :return: 200
    Question: What is your name?
    Answer: John
    Question: What is your age?
    Answer: 25
    Question: What is your gender?
    Answer: Male
    Question: What is your address?
    Answer: New York
    Question: What is your phone number?
    Answer: 1234567890
    Question: What is your email?
    Answer: john@gmail
    """
@profileBP.route('/verification', methods=['GET','POST'])
# @login_required
def verifiationOfUser():
    db, c = getDB()
    if request.method == 'GET':
        c.execute("SELECT * FROM profilequestion")
        questions = c.fetchall()
        return questions
    else:
        query = request.get_json()
        if isinstance(query, list):
            i = 0
            for i in range(len(query)):
                answer = query[i]['answer']
                c.execute("SELECT id FROM profileanswer ORDER BY id DESC LIMIT 1")
                id = c.fetchone()
                answer['id']=id['id'] + 1
                try:
                    message = answerController.createNewAnswer(answer)
                    print(message)
                except Exception as e:
                    return f"ERROR. {e}"
                
                uId = query[i]['userId']
                qId = query[i]['questionId']
                aId = answer['id']
                
                try:
                    c.execute(f"INSERT INTO `profileuserdetail`(`questionId`, `answerId`, `userId`) VALUES ('{qId}','{aId}','{uId}')")
                    db.commit()
                except Exception as e:
                    return f"ERROR. {e}"
                i+=1
        return "200"

        




@profileBP.route('/')
def indexUsers():
    return "INDEX PROFILE"
