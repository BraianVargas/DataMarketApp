from flask import Blueprint

answersBP = Blueprint('answers_BP', __name__)

from . import routes


