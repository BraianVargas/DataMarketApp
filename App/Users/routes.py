from flask import request,redirect,url_for
from flask_login import login_required, current_user,login_user,logout_user
from Commons.db import getDB

from .controller import *
from . import usersBP
from .models import User,users, get_user

#Esto solo es necesario para las pruebas
usuario=User(1, "Matias", "pepito@gmail.com", "lala1234")
users.append(usuario)

#Login
@usersBP.route('/login', methods=['GET', 'POST'])
def login():
    #Autentica si el usuario esta logeado
    if current_user.is_authenticated:
        return "ya inicioo sesion"
    
    #Si no esta logeado toma los datos del formulario
    user = request.args.get('user')
    password = request.args.get('password')
    remember_me = request.args.get('remember')
    #Esto simula la busqueda en la base de datos
    user = get_user(user)
    #Comprueba si el usuario existe y la contraseña es la misma
    if user is not None and user.check_password(password):
        #Loguea al usuario si todo funciono
        login_user(user, remember=remember_me)
        return "Se pudo loguear"
    #Avisa en caso de que no se pudiera loguear correctamente
    return "La contraseña o usuario estan mal"


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
    db, c = getDB()
    c.execute("SELECT * FROM users ORDER BY id ASC")
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

@usersBP.route('/new', methods = ["POST"])
@login_required # 
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

