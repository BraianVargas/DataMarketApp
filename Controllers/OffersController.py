import csv
from ..Classes.offers_class import Offers
from ..Commons.db import getDB

offersList = []

def commitDataList(dataList):
    # funcion para guardar archivo csv
    header = ["Offer_id" ,"Company Name" ,"Offer title" ,"Industry" ,"Type" ,"Verification" ,"reviews" ,"Applied Users" ,"Number of offers availables" ,"Number of offer left" ,"Company description" ,"Description" ,"Instructions" ,"Location" ,"Rewards" ,"picture"]
    
    with open('DataFiles/offers_data.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)
        
        # write the data
        for i in range(len(dataList)):
            writer.writerow(dataList[i].toList())
    
    return


def getOfferByIds(id):
    i = 0 
    c = getDB()
    
    c.execute('SELECT * FROM offers WHERE offerId = %s', (id,))
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
    
def createNewOffer(offersList, offerDict):
    newOffer = Offers( offerDict['offerId'], offerDict['companyName'], offerDict['offerTitle'], offerDict['industry'], offerDict['type'], offerDict['verification'], offerDict['reviews'], offerDict['appliedUsers'], offerDict['offersAvailables'], offerDict['offersLefts'], offerDict['companyDescription'], offerDict['description'], offerDict['instructions'], offerDict['location'], offerDict['rewards'], offerDict['picture'] )
    offersList.append(newOffer)
    commitDataList(offersList)
    return "202 - Status Ok - Offer Created"

def crearNuevaOferta(offerDict):
    newOffer = [offerDict['offerId'], offerDict['companyName'], offerDict['offerTitle'], offerDict['industry'], offerDict['type'], offerDict['verification'], offerDict['reviews'], offerDict['appliedUsers'], offerDict['offersAvailables'], offerDict['offersLefts'], offerDict['companyDescription'], offerDict['description'], offerDict['instructions'], offerDict['location'], offerDict['rewards'], offerDict['picture']]
    DataList(newOffer)
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