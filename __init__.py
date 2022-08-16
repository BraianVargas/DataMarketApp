from flask import Flask
from .Controllers.Modules import *

app = Flask(__name__)

objectList = []
objectList = readFile('DataFiles/offers_data.csv')

dictionaryList = []

@app.route("/")
def hello_world():
    return objectList

if __name__=='__main__':
    app.run(debug=True)
    app.run()