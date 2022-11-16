from Commons.db import getDB
from flask import request
from . import offersBP
from .controller import *
# ---------------------- GET routes ----------------------
@offersBP.route("/getOffers", methods=['GET'])
def getAll():
    db, c = getDB()
    c.execute("SELECT * FROM offers ORDER BY id ASC ")
    offers = c.fetchall()
    if offers!=None:
        return offers
    else:
        return "404 - Offer Not Found"
    
@offersBP.route('/filter/offerId/<offerId>')
def getOfferById(offerId):
    i = getOfferByIds(offerId)
    return i


@offersBP.route('/search', methods=['GET','POST'])
def getOf():
    #Se recibe el argumento como KEY
    OfferTitle = request.args.get('offer')
    #Se dividen los datos entrantes en una lista
    OfferTitle=OfferTitle.split()
    i = get_offers(OfferTitle)
    return i

# ---------------------- POST routes ----------------------
@offersBP.route('/crearOferta', methods=['POST'])
def crear():
    data = (request.get_json())
    statMessage = create_new_offer(data)
    print(statMessage)
    return statMessage

@offersBP.route('/deleteOffers/<id>', methods=['POST'])
def delete(id):
    statMessage = deleteOffers(id)
    return statMessage

@offersBP.route('/update/<id>', methods=['POST'])
def update(id):
    data = (request.get_json())
    statMessage = updateOffers(data,id)
    return statMessage