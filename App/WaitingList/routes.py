from flask import request,redirect,url_for, jsonify
from Commons.db import getDB

from .controller import *
from . import waitlistBP

@waitlistBP.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        data = request.get_json()
        info = joinController(data)
        return info
    else:
        return "join to the waiting list"
    
@waitlistBP.route("/enroled", methods=['GET'])
def get_waiters():
    if request.method == 'GET':
        data = getWaiters()
        return data
    else:
        return jsonify({'error': 'post method not allowed'}), 400
        