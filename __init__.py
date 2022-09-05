from flask import (
    Flask, request, g
    )

app = Flask(__name__)
app.config.from_pyfile("DataFiles/config.py")

from .Controllers.Modules import *
from .Commons.schema import *
from .Commons.db import getDB

offersList = []
offersList = readFile('DataFiles/offers_data.csv')

dictionaryList = []


# ---------------------- GET routes ----------------------
@app.route("/getOffers")
def getAll():
    db, c = getDB()
    c.execute("SELECT * FROM offers ORDER BY offerId ASC ")
    offers = c.fetchall()
    if offers!=None:
        return offers
    else:
        return "404 - Offer Not Found"
    

@app.route('/filter/offerId/<offerId>')
def getOfferById(offerId):
    i = getOfferByIds(offerId)
    return i

@app.route('/filter/company/<companyName> <industry> <type> <verification> <location> <rewards>', methods=['GET','POST'])
def getOfferByCompanyName(**kwargs):
    filters = None
    if request.method=='POST':
        filters = request.get_json()
        i = getFiltered(filters, **kwargs)
        return i
    else:
        i = getFiltered(**kwargs)
        return i

@app.route('/filter/industry/<industry>', methods=['GET'])
def getOfferByIndustry(industry):
    i = getIndustry(industry)
    return i
    

@app.route('/filter/type/<type>', methods=['GET'])
def getOfferByType(type):
    i = getType(type)
    return i



# ---------------------- POST routes ----------------------
@app.route('/create/offer', methods=['POST'])
def createOffer():
    data = (request.get_json())
    statMessage = createNewOffer(offersList, data)
    return statMessage


# if __name__=='__main__':
#     app.run(debug=True)
#     app.run()