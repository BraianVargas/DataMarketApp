import json

class Encoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

# def studentDecoder(obj):
#     if '__type__' in obj and obj['__type__'] == 'Student':
#         return Student(obj['rollNumber'], obj['name'], obj['marks'])
#     return obj
