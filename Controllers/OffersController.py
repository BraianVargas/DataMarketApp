import csv
from ..Classes.offers_class import Offers
from ..Commons.db import getDB

offersList = []

def getOfferByIds(id):
    i = 0 
    c = getDB()
    
    c.execute(f'SELECT * FROM offers WHERE offerId = {id}')
    offer = c.fetchone()
    if offer!=None:
        return offer
    else:
        return "404 - Offer Not Found"

def getOffer(filters, **kwargs):
    db, c = getDB()
    query = "SELECT * FROM offers"
    i = 0

    if kwargs != {}:
        print(kwargs)
        for key, value in kwargs.items():
            if i == 0:
                query += " WHERE "
            else:
                query += " || "
            query += "`{}`  '{}%'".format(key, value)
            query += " || "
            query += "`{}` LIKE '%{}'".format(key, value)
            query += " || "
            query += "`{}` LIKE '%{}%'".format(key, value)
            i+=1
    else:
        for key, value in filters.items():
            if i == 0:
                query += " WHERE "
            else:
                query += " || "
            query += "`{}` LIKE '{}%'".format(key, value)
            query += " || "
            query += "`{}` LIKE '%{}'".format(key, value)
            query += " || "
            query += "`{}` LIKE '%{}%'".format(key, value)
            # if isinstance(value, int):
            #     query += "{} LIKE {}".format(key, value)
            # else:
            i+=1
    print(query)
    c.execute(query)
    result = c.fetchall()

    if result != None:
        return result
    else:
        return "404 - Offer Not Found"

def getOffers(Title):
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

def createNewOffer(offerDict):
    db,c=getDB()
    # INSERT INTO offers (keys) VALUES (values)
    q = "INSERT INTO offers "
    keys =[] 
    values = []

    for key,value in offerDict.items():
        keys.append(key)
        values.append(value)
    i = 0
    q += "("
    for key in keys:
        if key == keys[len(keys) -1]:
            q += f"`{key}`"
        else:
            q += f"`{key}`, "
    q += ")"

    q += " VALUES "
    
    q += "("
    i=0
    for value in values:
        if value == values[len(values) -1]:
            q += f"`{value}`"
        else:
            q += f"`{value}`, "
    q += ")"

    print(q)
    c.execute(q)

    return "202 - Status Ok - Offer Created"

def DataList(data):
    db, c = getDB()
    #"INSERT INTO offers(offerId,created_at, companyName, offerTitle, industry, type, verification, reviews, appliedUsers, offersAvailables, offersLefts, companyDescription, description, instructions, location, rewards, picture) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data
    #query = "INSERT INTO offers (offerId, created_at, companyName, offerTitle, industry, type, verification, reviews, appliedUsers, offersAvailables, offersLefts, companyDescription, description, instructions, location, rewards, picture) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data
    try:
        c.execute("INSERT INTO offers (offerId, created_at, companyName, offerTitle, industry, type, verification, reviews, appliedUsers, offersAvailables, offersLefts, companyDescription, description, instructions, location, rewards, picture) VALUES(%s,'0000-00-00 00:00:00',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
        print("se pudo")
    except Exception as e:
        print(e)
    
    return