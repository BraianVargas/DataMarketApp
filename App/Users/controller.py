from Commons.db import getDB

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
    #Carga los datos en la db
    try:
        c.execute(q)
        db.commit()
    except Exception as e:
        print(e)
        return F"FATAL ERROR. {e}"
    return "202 - Status Ok - User Created"