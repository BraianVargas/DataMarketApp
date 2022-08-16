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
        self.__offerId = offerId
        self.__companyName = companyName
        self.__offerTitle = offerTitle
        self.__industry = industry
        self.__type = type
        self.__verification = verification
        self.__reviews = reviews
        self.__appliedUsers = appliedUsers
        self.__offersAvailables = offersAvailables
        self.__offersLefts = offersLefts
        self.__companyDescription = companyDescription
        self.__description = description
        self.__instructions = instructions
        self.__location = location
        self.__rewards = rewards
        self.__picture = picture
    
    