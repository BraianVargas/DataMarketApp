from flask import Blueprint

offersBP = Blueprint('offersBP', __name__)

from . import routes


