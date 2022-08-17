import csv
# from Classes.offers_class import *
from ..Classes.offers_class import Offers

offersList = []

def readFile(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            offer = Offers(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
            offersList.append(offer.__dict__)
    return offersList

def getByOfferIds(id):
    i = 0 
    while i < len(offersList) and int(id) != int(offersList[i]['_Offers__offerId']):
        i+=1
    if i<len(offersList):
        return i
    else:
        return "404 error - Offer Not Found"