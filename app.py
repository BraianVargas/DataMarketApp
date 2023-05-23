from flask import (
    Flask, request, g
    )

app = Flask(__name__)
app.config.from_pyfile("DataFiles/config.py")

from Commons.schema import *
from Commons.db import getDB
from flask_login import LoginManager
from App.Users.models import users

# ----------------------------- IMPORTA Y REGISTRA LOS BLUEPRINTS --------------------------------------
from App.Users import usersBP
app.register_blueprint(usersBP, url_prefix = '/users')

from App.Profile import profileBP
app.register_blueprint(profileBP, url_prefix = '/profile')

from App.Profile.Surveys.Questions import questionsBP
app.register_blueprint(questionsBP, url_prefix = '/questons')

from App.Profile.Surveys.Answers import answersBP
app.register_blueprint(answersBP, url_prefix = '/answers')

from App.Offers import offersBP
app.register_blueprint(offersBP, url_prefix = '/offers')

@app.route('/indexes')
def getUsers():
    return "API OK"

# ----------------------------- GENERA EL ADMINISTRADOR DE LOGIN --------------------------------------
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

@app.errorhandler(404)
def page_not_found(error):
    # Esta función se ejecutará cuando se encuentre un error 404
    return 'Página no encontrada', 404




if __name__=='__main__':
    app.run(debug=True)
    app.run()