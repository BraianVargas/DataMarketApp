from flask import Blueprint

waitlistBP = Blueprint('waitlist_BP', __name__)

from . import routes


