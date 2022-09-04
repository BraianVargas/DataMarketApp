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
    c.execute(
        """ 
        SELECT
            offerId,
            created_at,
            companyName,
            offerTitle,
            industry,
            type,
            verification,
            reviews,
            appliedUsers,
            offersAvailables,
            offersLefts,
            companyDescription,
            description,
            instructions,
            location,
            rewards,
            picture
        FROM offers ORDER BY offerId DESC
        """
    )
    todos = c.fetchall()
    print(todos)
    return todos
    # for i in range(len(offersList)):
    #     dictionaryList.append(offersList[i].toJSON())
    # return dictionaryList

@app.route('/filter/offerId/<offerId>')
def getOfferById(offerId):
    i = getOfferByIds(offerId)
    return i

@app.route('/filter/company/<companyName>')
def getOfferByCompanyName(companyName):
    i = getCompany(companyName)
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