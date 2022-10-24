from flask import Blueprint

profileBP = Blueprint('profile_BP', __name__)

from . import routes


