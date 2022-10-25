from flask import Blueprint

questionsBP = Blueprint('questions_BP', __name__)

from . import routes


