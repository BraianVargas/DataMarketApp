from Commons.db import getDB
from flask import request
from . import offersBP
from .controller import *
import json
from flask import Flask, jsonify


# ---------------------- GET routes ----------------------
@offersBP.route("/getOffers", methods=['GET'])
def getAll():
    try:
        db, c = getDB()
        c.execute("SELECT * FROM offers ORDER BY id ASC ")
        rows = c.fetchall()

        # Convert bytes objects to strings in each row of the result
        offers = []
        for row in rows:
            offer = dict(row)  # Convert the tuple to a dictionary
            for key, value in offer.items():
                if isinstance(value, bytes):
                    offer[key] = value.decode('utf-8')  # Convert bytes to string
            offers.append(offer)

        if offers:
            # Return a JSON response with the "application/json" Content-Type header
            return jsonify(offers)
        else:
            # Use the appropriate HTTP status code (404 Not Found)
            return jsonify(message="Offer Not Found"), 404
    except Exception as e:
        # Handle any database connection or query errors gracefully
        return jsonify(message="Error occurred: {}".format(str(e))), 500

    
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
    id = request.args.get('id')
    try:
        print(id)
        offer = getOfferById(int(id))
        return offer
        
    except Exception as e:
        print(e)
        return F"FATAL ERROR. {e}"
    # statMessage = updateOffers(int(id))