from flask import request,redirect,url_for
from flask_login import login_required, current_user,login_user,logout_user
from App.Profile import profileBP
from Commons.db import getDB

from flask_cors import CORS, cross_origin

from .controller import *
from .Surveys.Answers import controller as answerController

# ----------------------------- BUSQUEDAS Y FILTROS --------------------------------------
<<<<<<< HEAD
"""
It gets all the users from the database and returns them.
:return: A list of tuples.
"""
=======
>>>>>>> 31217065ed7beac5c629994b50f44f65f982966e
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
@profileBP.route('/verification', methods=['GET','POST'])
# @login_required
@cross_origin()
def verifiationOfUser():
    # se hace uso de la tabla 'profileUserDetail' como 'Fact Table'  
    # la cual va a guardar los id de las operaciónes de las questions y answers 
    # que se encuentran en las tablas 'questionSurvey' y 'answerSurvey'
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
<<<<<<< HEAD

=======
>>>>>>> development
                i+=1
        userVerification(query, query[-1]["userId"])
        return "200"


<<<<<<< HEAD
=======

@profileBP.route('/verification/<questionGroup>', methods=['GET','POST'])
def verificationByGroup(questionGroup):
    db, c = getDB()
    try:
        if request.method == "GET":
            try:
                data = getDataOfGroup(questionGroup)
                return data
            except:
                return "Error calling an DDBB question."
        else:
            query = request.get_json()
            print(query)
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
                    i+=1
            userVerification(query, query[-1]["userId"])
            return "200"
    except Exception as e:
        return f"Error al ejecutar la verificació de usuario. \n {e}"

        
>>>>>>> development




@profileBP.route('/')
def indexUsers():
    return "INDEX PROFILE"

