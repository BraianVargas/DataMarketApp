from flask import request,redirect,url_for, jsonify
from Commons.db import getDB

from .controller import *
from . import waitlistBP

@waitlistBP.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        return "page not found"
    else:
        data = request.get_json()
        info = joinController(data)
        return info