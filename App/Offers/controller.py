import csv
from Commons.db import getDB

def getOfferByIds(id):
    i = 0 
    db, c = getDB()
    
    c.execute(f'SELECT * FROM offers WHERE id = %s', (id,))
    offer = c.fetchone()
    if offer!=None:
        return offer
    else:
        return "404 - Offer Not Found"

def get_offers(offerDict):
    db, c = getDB()
    filtered=[]
    #Se buscan todas las coincidencias de offerTitle
    query = "SELECT * FROM offers WHERE "
    flag = 0 # Bandera de posicion inicial
    try:
        for key,value in offerDict.items():
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
            return "404 - Offer Not Found"
    except Exception as e:
        return f"Fatal Error. {e}"   


def getOffersByUserId(userId):
    db, c = getDB()
    try:
        c.execute(f'SELECT * FROM offers WHERE idCreator = %s', (userId,))
        filtered=c.fetchall()
        return filtered
    except Exception as e:
        return f"Fatal Error. {e}"   


def create_new_offer(offerDict):
    db,c=getDB()
    # Crea la query por medio de las KEY y las values ingresadas
    q = "INSERT INTO offers "
    keys =[] 
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
    return "202 - Status Ok - Offer Created"
    
def deleteOffers(offerId):
    db,c=getDB()
    try:
        c.execute("DELETE FROM `offers` WHERE id=%s",(offerId,))
        db.commit()
        return "202 - Status Ok - Offer Delete"
    except Exception as e:
        print(e)
        return F"FATAL ERROR. {e}"
        
def updateOffers(offers,id, idCreator):
    db,c=getDB()
    keys =[]
    values = []
    q = "UPDATE `offers` SET "
    for key,value in offers.items():
        keys.append(key)
        values.append(value)
    for key,value in offers.items():
        if key == keys[-1]:
            q += f"`{key}`='{value}'"
        else:
            q += f"`{key}`='{value}', "
    q += f" WHERE id={id} AND idCreator={idCreator}"
    try:
        c.execute(q)
        db.commit()
    except Exception as e:
        print(e)
        return F"FATAL ERROR. {e}"
    return "202 - Status Ok - Offer Updated"