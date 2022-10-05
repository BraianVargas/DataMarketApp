CREATE TABLE `offers` (
    `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `companyName` varchar(50) DEFAULT NULL,
    `offerTitle` varchar(50) DEFAULT NULL,
    `industry` varchar(50) DEFAULT NULL,
    `type` varchar(50) DEFAULT NULL,
    `verification` tinyint(1) DEFAULT NULL,
    `reviews` varchar(50) DEFAULT NULL,
    `appliedUsers` varchar(50) DEFAULT NULL,
    `offersAvailables` varchar(50) DEFAULT NULL,
    `offersLefts` varchar(50) DEFAULT NULL,
    `companyDescription` text DEFAULT NULL,
    `description` text DEFAULT NULL,
    `instructions` varchar(50) DEFAULT NULL,
    `location` varchar(50) DEFAULT NULL,
    `rewards` varchar(50) DEFAULT NULL,
    `picture` varchar(50) DEFAULT NULL,
    `idCreator` int DEFAULT NULL
);

CREATE TABLE `paymentinformation` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `linkedWallet` text DEFAULT NULL,
  `linkedSecundaryWallet` text DEFAULT NULL,
  `linkedBankAccountName` text DEFAULT NULL,
  `linkedBankAccountNumber` int(11) DEFAULT NULL
);

CREATE TABLE `surveyquery` (
    `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `content` text DEFAULT NULL,
    `answerId` int DEFAULT NULL, 
    `creatorId` int DEFAULT NULL
);

CREATE TABLE `surveyanswer` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `content` text DEFAULT NULL,
    `queryId` int DEFAULT NULL, 
    `creatorId` int DEFAULT NULL
);

CREATE TABLE `users` (
    `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `name` varchar(50) NOT NULL,
    `nickname` varchar(50) NOT NULL,
    `lastName` varchar(50) NOT NULL,
    `email` varchar(50) NOT NULL,
    `address` varchar(50) NOT NULL,
    `state` varchar(50) NOT NULL,
    `postCode` varchar(50) NOT NULL,
    `phoneNumber` varchar(50) NOT NULL,
    `country` varchar(50) NOT NULL,
    `password` varchar(255) NOT NULL,
    `role` varchar(50) NOT NULL DEFAULT "user",
    `offerId` int DEFAULT NULL,
    `surveyQuery` int DEFAULT NULL,
    `surveyAnswer` int DEFAULT NULL,
    `paymentInformation` int DEFAULT NULL
);



ALTER TABLE offers ADD FOREIGN KEY(`idCreator`) REFERENCES users(id);
ALTER TABLE users ADD FOREIGN KEY(`offerId`) REFERENCES offers(id);
ALTER TABLE users ADD FOREIGN KEY(`surveyQuery`) REFERENCES surveyquery(id);
ALTER TABLE users ADD FOREIGN KEY(`surveyAnswer`) REFERENCES surveyanswer(id);
ALTER TABLE users ADD FOREIGN KEY(`paymentInformation`) REFERENCES paymentinformation(id);
ALTER TABLE surveyquery ADD FOREIGN KEY(`answerId`) REFERENCES surveyanswer(id);
ALTER TABLE surveyquery ADD FOREIGN KEY(`creatorId`) REFERENCES users(id);
ALTER TABLE surveyanswer ADD FOREIGN KEY(`queryId`) REFERENCES surveyquery(id);
ALTER TABLE surveyanswer ADD FOREIGN KEY(`creatorId`) REFERENCES users(id);