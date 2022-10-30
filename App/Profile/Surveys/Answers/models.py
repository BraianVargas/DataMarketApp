class Answers:
    answerName = None
    answerGroup = None
    answerGroupDisplay = None
    answerDescription = None
    answerType = None
    answerOptionId = None
    additionalComments = None
    
    def __init__(self, answerName, answerGroup, answerGroupDisplay, answerDescription, answerType, answerOptionId, additionalComments):
        self.answerName = answerName
        self.answerGroup = answerGroup
        self.answerGroupDisplay = answerGroupDisplay
        self.answerDescription = answerDescription
        self.answerType = answerType
        self.answerOptionId = answerOptionId
        self.additionalComments = additionalComments
        