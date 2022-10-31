from flask import request,redirect,url_for
from flask_login import login_required, current_user,login_user,logout_user
from App.Profile import profileBP
from Commons.db import getDB

from .controller import *

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
# se hace uso de la tabla 'profileUserDetail' como 'Fact Table'  
# la cual va a guardar los id de las operaciónes de las questions y answers 
# que se encuentran en las tablas 'questionSurvey' y 'answerSurvey'

@profileBP.route('/verification', methods=['GET','POST'])
# @login_required
def verifiationOfUser():
    db, c = getDB()
    if request.method == 'GET':
        c.execute("SELECT * FROM profileQuestion")
        questions = c.fetchall()
        return questions
    else:
        query = request.get_json()
        if isinstance(query, list):
            i = 0
            answer = query[i]['answer']
            for i in range(len(query)):
                print(f"************ ANSWER {answer} ************* ")

                # q = c.execute("SELECT * FROM profileanswer ORDER BY id DESC LIMIT 1")
        return answer

        
@profileBP.route('/')
def indexUsers():
    return "INDEX PROFILE"
