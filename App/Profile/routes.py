from flask import request,redirect,url_for
from flask_login import login_required, current_user,login_user,logout_user
from App.Users import usersBP
from Commons.db import getDB

from .controller import *

# ----------------------------- PASAR A PROFILE --------------------------------------
# ----------------------------- CAMBIAR LAS RUTAS Y MÉTODOS PARA REFERIRLOS DE usersBP a profileBP --------------------------------------



# ----------------------------- BUSQUEDAS Y FILTROS --------------------------------------
@usersBP.route('/getusers', methods=["GET","POST"])
# @login_required
def getUsers():
    db, c = getDB()
    c.execute("SELECT * FROM profile ORDER BY id ASC")
    users = c.fetchall()

    if users != None:
        return users
    else:
        return "404 - User Table Is Empty"

@usersBP.route("/search", methods=['GET','POST'])
@login_required
def searchUser():
    #Se recibe el argumento como KEY
    i = get_users(request.get_json())
    return i

@usersBP.route('/questions/new', methods = ["POST"])
# @login_required 
def createUser():
    #
    # if is logged in as administrator
    #
    data = request.get_json()

    message = createNewUser(data)

    return message

# ----------------------------- VERIFICACIÓN DE USUARIO --------------------------------------
@usersBP.route('/verification', methods=['GET','POST'])
# @login_required
def verifiationOfUser():
    # se hace uso de la tabla 'profileUserDetail' como 'Fact Table'  
    # la cual va a guardar los id de las operaciónes de las questions y answers 
    # que se encuentran en las tablas 'questionSurvey' y 'answerSurvey'
    db, c = getDB()
    if request.method == 'GET':
        query = c.execute("SELECT * FROM profileQuestion")
        questions = c.fetchall()
        return questions
    else:
        return None


@usersBP.route('/')
def indexUsers():
    return "INDEX USER"

