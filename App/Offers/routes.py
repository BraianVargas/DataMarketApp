from Commons.db import getDB
from flask import *
from . import offersBP
from .controller import *
import time

from flask_login import *
# ---------------------- GET routes ----------------------
@offersBP.route("/getOffers", methods=['GET'])
@login_required
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
@login_required
def delete(id):
    statMessage = deleteOffers(id)
    return statMessage

@offersBP.route('/update', methods=['GET','POST'])
@login_required
def update():
    data = []
    if request.method == 'GET':
        try:
            offerId = request.args.get('id')
            if current_user.is_authenticated:
                data = getOffersByUserId(current_user.get_id())
                return data
            else:
                return "23"
        except Exception as e:
            return f"Update error. {e}"
    else:
        if request.method == 'POST':
            offerId = request.args.get('id')
            data = request.get_json()
            statMessage = updateOffers(data,int(offerId))
            return statMessage
        else:
            return "234"