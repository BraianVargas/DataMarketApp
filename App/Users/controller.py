from Commons.db import getDB
import hashlib
from .models import User

def createNewUser(offerDict):
    db,c = getDB()

    q = "INSERT INTO users "
    keys = []
    values = []    
    for key,value in offerDict.items():
        keys.append(key)
        values.append(value)
    q += "("
    for key in keys:
        if key == keys[-1]:
            q += f"{key}"
        else:
            q += f"{key},"
    q += ")"
    q += " VALUES"
    q += "("
    for value in values:
        if value == values[-1]:
            q += f"'{value}'"
        elif type(value) == int or type(value) == float:
            q += f"{value},"
        else:
            q += f"'{value}',"
    q += ")"
    try:
        c.execute(q)
        db.commit()
        return "202 - Status Ok - User Created"
    except Exception as e:
        print(e)
        return F"FATAL ERROR. {e}"

def getUserFromLogin(uname, inputPassword):
    db, c = getDB()
    try:
        c.execute(f"SELECT * FROM users WHERE username = %s",(uname,))
        userSelected = c.fetchone()
        if userSelected != None:
            try:
                if userSelected['password'] == (hashlib.sha512(inputPassword.encode())).hexdigest():
                    try:
                        return User(userSelected['id'], userSelected['username'], userSelected['role'], userSelected['password'])
                    except Exception as e:
                        return f"User error: {e}"
                else:
                    return "Error. User or password not match."    
            except Exception as e:
                return f"Error in Password: {e}"
        else:
            return "Error. User not found."
    except Exception as e:
        return f"Error in username: {e}"

def getAllUsers():
    db, c = getDB()
    c.execute("SELECT * FROM users ORDER BY id ASC")
    users = c.fetchall()
    return users

def get_users(userDict):
    db, c = getDB()
    filtered=[]
    query = "SELECT * FROM users WHERE "
    flag = 0 # Bandera de posicion inicial
    try:
        for key,value in userDict.items():
            if flag == 0:
                query += f" {key} LIKE '%{value}%' "
                flag += 1
            else:
                query += f" || {key} LIKE '%{value}%' "
        c.execute(query)
        filtered = c.fetchall()
        if filtered != None:
            return filtered
        else:
            return "404 - User Not Match"
    except Exception as e:
        return f"Fatal Error. {e}"

# ----------------------------- USER VERIFICATION --------------------------------------

def userVerification():
    db, c = getDB()
    questions = []
    query = "SELECT * FROM "
