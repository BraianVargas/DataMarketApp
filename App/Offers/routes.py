from Commons.db import getDB
from flask import request, session
from . import offersBP
from .controller import *
import time

from flask_login import *
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
@login_required
def update():
    offerId = request.args.get('id')
    if request.method=='GET':
        if current_user.is_authenticated:
            offerDict = dict(id = offerId, idCreator = current_user.get_id())
            print(offerDict)
            time.sleep(20000)
            get_offers()
    else:
        statMessage = updateOffers(data,int(id))
        return statMessage