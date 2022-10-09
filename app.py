from flask import (
    Flask, request, g
    )

app = Flask(__name__)
app.config.from_pyfile("DataFiles/config.py")

from Commons.schema import *
from Commons.db import getDB


# importa el blueprint y lo registra
from App.Users import usersBP
app.register_blueprint(usersBP, url_prefix = '/users')





if __name__=='__main__':
    app.run(debug=True)
    app.run()