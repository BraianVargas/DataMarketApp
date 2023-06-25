from flask import jsonify
from Commons.db import getDB

def joinController(offerDict):
    db,c = getDB()
    name = offerDict.get('name')
    email = offerDict.get('email')
    phone = offerDict.get('phone')

    if not name or not email:
        return jsonify({'error': 'Name and email are required.'}), 400

    # Store in the MySQL database (DDBB: datamarket - Table: waiting_list)
    cursor = db.cursor()
    query = "INSERT INTO waiting_list (name, email, phone) VALUES (%s, %s, %s)"
    values = (name, email, phone)
    cursor.execute(query, values)
    db.commit()

    return 'Successfully added to the waiting list.'
