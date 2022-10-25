from Commons.db import getDB

# ----------------------------- PROFILE SURVEY --------------------------------------

def createNewQuestion(offerDict):
    db,c = getDB()

    q = "INSERT INTO profilequestion "
    keys = []
    values = []    
    for key,value in offerDict.items():
        keys.append(key)
        values.append(value)
    q += "("
    for key in keys:
        if key == keys[-1]:
            q += f"`{key}`"
        else:
            q += f"`{key}`,"
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
        print(q)
        c.execute(q)
        db.commit()
        return "202 - Status Ok - Profile questions loaded succesfully"
    except Exception as e:
        print(e)
        return F"FATAL ERROR. {e}"







# ----------------------------- USER VERIFICATION --------------------------------------

def userVerification():
    db, c = getDB()
    questions = []
    query = "SELECT * FROM "