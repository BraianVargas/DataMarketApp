from flask import (
    Flask, request, g
    )

app = Flask(__name__)
app.config.from_pyfile("DataFiles/config.py")

from Commons.schema import *
from Commons.db import getDB
from flask_login import LoginManager
from App.Users.models import users

# importa el blueprint y lo registra
from App.Users import usersBP
app.register_blueprint(usersBP, url_prefix = '/users')

#genera el administrar de logeo
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None





if __name__=='__main__':
    app.run(debug=True)
    app.run()