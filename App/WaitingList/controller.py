from flask import jsonify
from Commons.db import getDB

def joinController(offerDict):
    db,c = getDB()
    
    firstname =  offerDict.get('firstname')
    lastname =  offerDict.get('lastname')
    job_title =  offerDict.get('job_title')
    company_name =  offerDict.get('company_name')
    business_email =  offerDict.get('business_email')
    phone =  offerDict.get('phone')
    country	 =  offerDict.get('country')

    if not firstname or not business_email:
        return jsonify({'error': 'Name and email are required.'}), 400

    # Store in the MySQL database (DDBB: datamarket - Table: waiting_list)
    cursor = db.cursor()
    query = """INSERT INTO waitlist (
            firstname, 
            lastname, 
            job_title, 
            company_name, 
            business_email, 
            phone, 
            country
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s )"""
    
    values = (
        firstname,
        lastname,
        job_title,
        company_name,
        business_email,
        phone,
        country
    )
    cursor.execute(query, values)
    db.commit()

    return 'Successfully added to the waiting list.'
