
# ---------------------- GET routes ----------------------
@app.route("/getOffers")
def getAll():
    db, c = getDB()
    c.execute("SELECT * FROM offers ORDER BY id ASC ")
    offers = c.fetchall()
    if offers!=None:
        return offers
    else:
        return "404 - Offer Not Found"
    
@app.route('/filter/offerId/<offerId>')
def getOfferById(offerId):
    i = getOfferByIds(offerId)
    return i


@app.route('/search/', methods=['GET','POST'])
def getOf():
    #Se recibe el argumento como KEY
    OfferTitle = request.args.get('offer')
    #Se dividen los datos entrantes en una lista
    OfferTitle=OfferTitle.split()
    i = get_offers(OfferTitle)
    return i

# ---------------------- POST routes ----------------------
@app.route('/crearOferta', methods=['POST'])
def crear():
    data = (request.get_json())
    statMessage = create_new_offer(data)
    print(statMessage)
    return statMessage