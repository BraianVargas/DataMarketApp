import csv
from ..Classes.offers_class import Offers
from ..Commons.db import getDB

def getOfferByIds(id):
    i = 0 
    c = getDB()
    
    c.execute('SELECT * FROM offers WHERE offerId = %s', (id,))
    offer = c.fetchone()
    if offer!=None:
        return offer
    else:
        return "404 - Offer Not Found"

def get_offers(Title):
    db, c = getDB()
    filtered=[]
    #Se buscan todas las coincidencias de offerTitle
    query = "SELECT * FROM offers WHERE "
    for title in Title:
        if title == Title[0]:
            query += f" offerTitle LIKE '%{title}%' "
        else:
            query += f" || offerTitle LIKE '%{title}%' "
    c.execute(query)
    filtered = c.fetchall()
    if filtered != None:
        return filtered
    else:
        return "404 - Offer Not Found"
    
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
        return "NO SE PUDO CREAR LA OFERTA"
    return "202 - Status Ok - Offer Created"
    
    