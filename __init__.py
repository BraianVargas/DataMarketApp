from flask import (
    Flask, request, g
    )

app = Flask(__name__)
app.config.from_pyfile("DataFiles/config.py")

<<<<<<< HEAD
from .Controllers.Modules import *
=======
from .Controllers.OffersController import *
>>>>>>> fefecd345406a1454474e6b13cba329e31521d16
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
<<<<<<< HEAD
    if request.method=='POST':
        filters = request.get_json()
        i = getOffer(filters)
        return i
    else:
        filters = request.get_json()
        i = getOffer(filters)
        return i
=======
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
>>>>>>> fefecd345406a1454474e6b13cba329e31521d16

# ---------------------- POST routes ----------------------
@app.route('/createOffer', methods=['POST'])
def createOffer():
    data = (request.get_json())
    statMessage = createNewOffer(offersList, data)
    return statMessage

<<<<<<< HEAD
=======
@app.route('/crearOferta', methods=['POST'])
def crear():
    data = (request.get_json())
    statMessage = crearNuevaOferta(data)
    return statMessage

>>>>>>> fefecd345406a1454474e6b13cba329e31521d16

# if __name__=='__main__':
#     app.run(debug=True)
#     app.run()