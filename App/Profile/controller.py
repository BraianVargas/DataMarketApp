from Commons.db import getDB

def createNewProfile(offerDict):
    db,c = getDB()

    q = "INSERT INTO profile "
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


def get_users(userDict):
    db, c = getDB()
    filtered=[]
    query = "SELECT * FROM profile WHERE "
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
def userVerification(cantOfAnswers, userId):
    db, c = getDB()
    verified = 0

    c.execute(f"SELECT * FROM profileuserdetail WHERE userId={userId}")
    c.fetchall()

    completes = c.rowcount
    print(f"############### QUERY \n {completes} \n##############")

    c.execute("SELECT * FROM profilequestion")
    c.fetchall()
    cantOfQuestions = c.rowcount

    # COQ -> 100%
    # COA -> x => x=((COA*100)/COQ) => It is the  porcent of questions answered

    porcentComplete = (completes * 100)/cantOfQuestions
    print(f"porcentaje completado {porcentComplete}")


    porcentRemaining = (cantOfAnswers * 100)/cantOfQuestions
    print(f"porcentaje faltante {porcentRemaining}")
    
    total = porcentComplete + porcentRemaining
    print(f"porcentaje total {total}")

    if int(total) == 100:
        print(f"VERIFICADAZO")

    if completes == cantOfQuestions:
        print(f"VERIFICADAZO")

    if (porcentComplete + porcentRemaining) == 100:
        verified = 1
        c.execute(f"UPDATE `profile` SET `isVerified`='{verified}' WHERE `id` = '{userId}'")
        db.commit()
    
    return 200
    # UPDATE `profile` SET `isVerified`='[value-13]' WHERE `id` = '[value-13]'