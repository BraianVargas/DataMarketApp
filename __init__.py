from flask import (
    Flask, request, g
    )

app = Flask(__name__)
app.config.from_pyfile("DataFiles/config.py")

from .Controllers.OffersController import *
from .Commons.schema import *
from .Commons.db import getDB

offersList = []

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

@app.route('/filter/', methods=['GET','POST'])
def getFiltered():
    filters = None
    filters = request.get_json()
    i = getOffer(filters)
    return i


@app.route('/search/', methods=['GET','POST'])
def getOf():
    #Se recibe el argumento como KEY
    OfferTitle = request.args.get('offer')
    #Se dividen los datos entrantes en una lista
    OfferTitle=OfferTitle.split()
    i = getOffers(OfferTitle)
    return i

# ---------------------- POST routes ----------------------
@app.route('/crearOferta', methods=['POST'])
def crear():
    data = (request.get_json())
    statMessage = createNewOffer(data)
    return statMessage


# if __name__=='__main__':
#     app.run(debug=True)
#     app.run()