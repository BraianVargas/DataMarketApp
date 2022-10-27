from flask import request,redirect,url_for
from flask_login import login_required, current_user,login_user,logout_user
from App.Profile import profileBP
from Commons.db import getDB

from .controller import *

# ----------------------------- PASAR A PROFILE --------------------------------------
# ----------------------------- CAMBIAR LAS RUTAS Y MÉTODOS PARA REFERIRLOS DE usersBP a profileBP --------------------------------------



# ----------------------------- BUSQUEDAS Y FILTROS --------------------------------------
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
    #Se recibe el argumento como KEY
    i = get_users(request.get_json())
    return i

@profileBP.route('/new', methods = ["POST"])
# @login_required 
def createProfile():
    #
    # if is logged in as administrator
    #
    data = request.get_json()

    message = createNewProfile(data)

    return message

# ----------------------------- VERIFICACIÓN DE USUARIO --------------------------------------
@profileBP.route('/verification', methods=['GET','POST'])
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


@profileBP.route('/')
def indexUsers():
    return "INDEX PROFILE"

