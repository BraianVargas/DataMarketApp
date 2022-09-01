import csv
import json
from ..Classes.offers_class import Offers

offersList = []

def readFile(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            offer = Offers(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
            offersList.append(offer)
    return offersList

def commitDataList(dataList):
    # funcion para guardar archivo csv
    header = ["Offer_id" ,"Company Name" ,"Offer title" ,"Industry" ,"Type" ,"Verification" ,"reviews" ,"Applied Users" ,"Number of offers availables" ,"Number of offer left" ,"Company description" ,"Description" ,"Instructions" ,"Location" ,"Rewards" ,"picture"]
    
    with open('DataFiles/offers_data.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        print("dataList")
        print(dataList)
        # write the data
        for i in range(len(dataList)):
            writer.writerow(dataList[i].toList())
    
    return

def getOfferByIds(id):
    i = 0 
    while ((i < len(offersList)) and ((int(id) != int(offersList[i].toJSON()['offerId'])))):
        i+=1
    if i<len(offersList):
        return(offersList[i].toJSON())
    else:
        return "404 - Offer Not Found"

        
def getCompany(companyName):
    i = 0 
    listOfOffers = []
    while (i < len(offersList)):
        if ((companyName.lower() == offersList[i].toJSON()['companyName'].lower())):
            listOfOffers.append(offersList[i].toJSON())
            i+=1
        else:
            i+=1
    if listOfOffers != None:
        return listOfOffers
    else:
        return "404 - Offer Not Found"
        
def getType(type):
    i = 0 
    listOfOffers = []
    while (i < len(offersList)):
        if ((type.lower() == offersList[i].toJSON()['type'].lower())):
            listOfOffers.append(offersList[i].toJSON())
            i+=1
        else:
            i+=1
    if listOfOffers != None:
        return listOfOffers
    else:
        return "404 - Offer Not Found"

def getIndustry(industry):
    i = 0 
    listOfOffers = []
    while (i < len(offersList)):
        if(((industry.lower() == offersList[i].toJSON()['industry'].lower()))):
            listOfOffers.append(offersList[i].toJSON())
            i+=1
        else:
            i+=1
    if listOfOffers != None:
        return listOfOffers
    else:
        return "404 - Offer Not Found"

def createNewOffer(offersList, offerDict):
    newOffer = Offers( offerDict['offerId'], offerDict['companyName'], offerDict['offerTitle'], offerDict['industry'], offerDict['type'], offerDict['verification'], offerDict['reviews'], offerDict['appliedUsers'], offerDict['offersAvailables'], offerDict['offersLefts'], offerDict['companyDescription'], offerDict['description'], offerDict['instructions'], offerDict['location'], offerDict['rewards'], offerDict['picture'] )
    offersList.append(newOffer)
    commitDataList(offersList)
    return "202 - Status Ok - Offer Created"