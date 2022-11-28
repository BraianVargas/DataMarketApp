from Commons.db import getDB
from flask import request, session
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
@offersBP.route('/create', methods=['POST'])
def crear():
    data = (request.get_json())
    statMessage = create_new_offer(data)
    return statMessage

@offersBP.route('/delete/<id>', methods=['POST'])
def delete(id):
    statMessage = deleteOffers(id)
    return statMessage

@offersBP.route('/update', methods=['PUT', 'GET'])
def update():
    data = request.args.get('id')
    if request.method=='GET':
        if "username" in session and "role" in session:
            return data
    else:
        statMessage = updateOffers(data,int(id))
        return statMessage