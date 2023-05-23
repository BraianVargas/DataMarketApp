from Commons.db import getDB
import json

def createNewProfile(offerDict):
    db,c = getDB()

    q = "INSERT INTO profile "
    keys = []
    values = []    
    for key,value in offerDict.items():
        keys.append(key)
        values.append(value)
    q += "("
    for key in keys:
        if key == keys[-1]:
            q += f"{key}"
        else:
            q += f"{key},"
    q += ")"
    q += " VALUES"
    q += "("
    for value in values:
        if value == values[-1]:
            q += f"'{value}'"
        elif type(value) == int or type(value) == float:
            q += f"{value},"
        else:
            q += f"'{value}',"
    q += ")"
    try:
        c.execute(q)
        db.commit()
        return "202 - Status Ok - User Created"
    except Exception as e:
        print(e)
        return F"FATAL ERROR. {e}"


def get_users(userDict):
    db, c = getDB()
    filtered=[]
    query = "SELECT * FROM profile WHERE "
    flag = 0 # Bandera de posicion inicial
    try:
        for key,value in userDict.items():
            if flag == 0:
                query += f" {key} LIKE '%{value}%' "
                flag += 1
            else:
                query += f" || {key} LIKE '%{value}%' "
        c.execute(query)
        filtered = c.fetchall()
        if filtered != None:
            return filtered
        else:
            return "404 - User Not Match"
    except Exception as e:
        return f"Fatal Error. {e}"


# ----------------------------- USER VERIFICATION --------------------------------------

# -- Codigo de modelado de info para el GET de los datos y metadatos de las questions para la verificación de usuario
def getDataOfGroup(questionGroup):
    db, c = getDB()
    __metadata__ = [
        {'age': 'number'},
        {'contact': [
            {'phone': 'number'},
            {'mail': 'email'}
        ]},
        {'address': 'string'},
        {'name': 'string'},
        {'date-of-birth': 'date'}
    ]

    data = []

    try:
        c.execute(f"SELECT * FROM profilequestion WHERE questionGroup='{str(questionGroup).lower()}'")
        questions = c.fetchall()

        for question in questions:
            entry_metadata = {}

            if "user entry" in question['questionType'].lower():
                if questionGroup == "contact":
                    for meta in __metadata__:
                        if questionGroup in meta.keys():
                            contact_metadata = meta[questionGroup]
                            for contact_entry in contact_metadata:
                                for key, value in contact_entry.items():
                                    if key in question['questionDescription'] or key in question['questionName']:
                                        entry_metadata['typeEntry'] = value
                                        break
                                if 'typeEntry' in entry_metadata:
                                    break
                            if 'typeEntry' in entry_metadata:
                                break
                else:
                    for meta in __metadata__:
                        if questionGroup in meta.keys():
                            entry_metadata['typeEntry'] = meta[questionGroup]
                            break

                data.append({
                    'Datos': question,
                    'Metadatos': entry_metadata
                })

            elif "multiple choice" in question['questionType'].lower():
                c.execute(f"SELECT * FROM multiplechoiceoptions WHERE questionGroup='{str(questionGroup).lower()}'")
                options = c.fetchall()
                entry_metadata['Opciones'] = [option['optionContent'] for option in options]

                data.append({
                    'Datos': question,
                    'Metadatos': entry_metadata
                })

            else:
                return "Unknowed question group"

    except Exception as e:
        return f"Error requesting DDBB. \n{e}"

    return data

"""
It takes a list of answers and a userId, then it checks if the user has answered all the questions,
if so, it updates the user's profile to verified

:param answers: [{'questionId': 1, 'answer': {'id': 1, 'answer': 'Yes'}, 'userId': 1},
{'questionId': 2, 'answer': {'id': 2, 'answer': 'No'}, 'userId': 1}, {
:param userId: The user's ID
:return: A list of questions
"""
def userVerification(answers, userId):
    db, c = getDB()
    verified = 0
    c.execute(f"SELECT questionId FROM profileuserdetail WHERE userId={userId}")
    questionsIds = c.fetchall()
    listOfId = []
    i = 0
    while(i<len(questionsIds)):
        listOfId.append(questionsIds[i]["questionId"])
        i+=1
    i=0 
    while(i<len(answers)):
        if(answers[i]["questionId"] in listOfId):
            i+=1
            print("no se agregó elemento")
        else:
            uId = answers[i]['userId']
            qId = answers[i]['questionId']
            aId = answers[i]['answer']['id']

            c.execute(f"INSERT INTO `profileuserdetail`(`questionId`, `answerId`, `userId`) VALUES ('{qId}','{aId}','{uId}')")
            db.commit()
            
            listOfId.append(qId)
            i+=1

    c.execute("SELECT id FROM profilequestion")
    questionsIds = c.fetchall()

    listOfId2 = []
    i=0
    while(i<len(questionsIds)):
        listOfId2.append(questionsIds[i]["id"])
        i+=1

    if len(listOfId) == len(listOfId2):
        verified = 1
        c.execute(f"UPDATE `profile` SET `isVerified`='{verified}' WHERE `id` = '{userId}'")
        db.commit()
        print("Profile Verified")
    
    return 200