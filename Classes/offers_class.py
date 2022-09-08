import json
from pathlib import Path

class Offers:
    __offerId = None
    __companyName = None
    __offerTitle = None
    __industry = None
    __type = None
    __verification = None
    __reviews = None
    __appliedUsers = None
    __offersAvailables = None
    __offersLefts = None
    __companyDescription = None
    __description = None
    __instructions = None
    __location = None
    __rewards = None
    __picture = None

    def __init__(self, offerId, companyName, offerTitle, industry, type, verification, reviews, appliedUsers, offersAvailables, offersLefts, companyDescription, description, instructions, location, rewards, picture):
        self.__offerId = offerId #
        self.__companyName = companyName #
        self.__offerTitle = offerTitle
        self.__industry = industry #
        self.__type = type #
        self.__verification = verification # (Compañias verificadas)
        self.__reviews = reviews
        self.__appliedUsers = appliedUsers
        self.__offersAvailables = offersAvailables
        self.__offersLefts = offersLefts
        self.__companyDescription = companyDescription
        self.__description = description
        self.__instructions = instructions
        self.__location = location #
        self.__rewards = rewards # 
        self.__picture = picture
    

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            
            offerId = self.__offerId,
            companyName = self.__companyName,
            offerTitle = self.__offerTitle,
            industry = self.__industry,
            type = self.__type,
            verification = self.__verification,
            reviews = self.__reviews,
            appliedUsers = self.__appliedUsers,
            offersAvailables = self.__offersAvailables,
            offersLefts = self.__offersLefts,
            companyDescription = self.__companyDescription,
            description = self.__description,
            instructions = self.__instructions,
            location = self.__location,
            rewards = self.__rewards,
            picture = self.__picture

            # variable bla bla bla
            
        )
        return d

    def toList(self):
        return [
            self.__offerId,
            self.__companyName,
            self.__offerTitle,
            self.__industry,
            self.__type,
            self.__verification,
            self.__reviews,
            self.__appliedUsers,
            self.__offersAvailables,
            self.__offersLefts,
            self.__companyDescription,
            self.__description,
            self.__instructions,
            self.__location,
            self.__rewards,
            self.__picture
        ]