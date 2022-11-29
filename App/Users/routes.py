import datetime
from flask import request,redirect,url_for
from flask_login import login_required, current_user,login_user,logout_user
from Commons.db import getDB

from .models import User

from .controller import *
from . import usersBP
import time

#Login
@usersBP.route('/login', methods=['GET', 'POST'])
def login():
    #Autentica si el usuario esta logeado

    if current_user.is_authenticated:
        return "Is already logged in."
    else:
        #Si no esta logeado toma los datos del formulario
        username = request.args.get('username')
        password = request.args.get('password')
        remember_me = request.args.get('remember')
        
        try:
            #Esto realiza la busqueda en la base de datos
            user = getUserFromLogin(username, password)
            #Comprueba si el usuario existe y la contraseña es la misma
            if ((user!=None) and (isinstance(user,User))):
                login_user(user, remember = remember_me, duration = datetime.timedelta(hours = 7))
                return "Se pudo loguear"
        except Exception as e:
            #Avisa en caso de que no se pudiera loguear correctamente
            return f"User or password wrong. Error.{e}"

#Desloguea al usuario

@usersBP.route('/logout')
@login_required
def logout():
    logout_user()
    return "Cerro sesion"


@usersBP.route('/register')
def registerUser():
    data = (request.get_json())
    statMessage = createNewUser(data)
    print(statMessage)
    return statMessage


# ----------------------------- BUSQUEDAS Y FILTROS --------------------------------------

@usersBP.route('/getusers', methods=["GET","POST"])
@login_required
def getUsers():
    users = getAllUsers()
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

@usersBP.route('/new', methods = ["POST"])
@login_required 
def createUser():
    #
    # if is logged in as administrator
    #
    data = request.get_json()

    message = createNewUser(data)

    return message

# ----------------------------- VERIFICACIÓN DE USUARIO --------------------------------------
@usersBP.route('/verification', methods=['GET','POST'])
@login_required
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
@login_required
def indexUsers():
    return "INDEX USER"
