from re import S
from flask import Flask
import json
from .Controllers.Modules import *

app = Flask(__name__)

objectList = []
objectList = readFile('DataFiles/offers_data.csv')

dictionaryList = []

@app.route("/getOffers")
def getAll():
    return objectList

@app.route('/filter/offerId/<offerId>')
def getByOfferId(offerId):
    i = getByOfferIds(offerId)
    if isinstance(i, int):
        # return json.dumps(objectList[i])
        return objectList[i]
    else:
        return i

# if __name__=='__main__':
#     app.run(debug=True)
#     app.run()