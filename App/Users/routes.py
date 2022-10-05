from flask import request
from flask_login import login_required, current_user
from Commons.db import getDB


from .controller import createNewUser
from . import usersBP

@usersBP.route('/getusers', methods=["GET","POST"])
def getUsers():
    db, c = getDB()
    c.execute("SELECT * FROM users ORDER BY id ASC")
    users = c.fetchall()

    if users != None:
        return users
    else:
        return "404 - User Table Is Empty"

@usersBP.route('/new', methods = ["POST"])
def createUser():
    #
    # if is logged in as administrator
    #
    data = request.get_json()

    message = createNewUser(data)

    return message
    
@usersBP.route('/')
def indexUsers():
    return "INDEX USER"

    
@usersBP.route('/new', methods = ["GET","POST"])
def createUser():
    #
    # if is logged in as administrator
    #
    data = request.get_json()

    message = createNewUser(data)

    return message
    
@usersBP.route('/')
def indexUsers():
    return "INDEX USER"