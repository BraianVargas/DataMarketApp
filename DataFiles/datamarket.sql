CREATE TABLE `offers` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `companyName` TEXT DEFAULT NULL,
    `offerTitle` TEXT DEFAULT NULL,
    `industry` TEXT DEFAULT NULL,
    `type` TEXT DEFAULT NULL,
    `verification` TINYINT(1) DEFAULT NULL,
    `reviews` TEXT DEFAULT NULL,
    `appliedUsers` TEXT DEFAULT NULL,
    `offersAvailables` TEXT DEFAULT NULL,
    `offersLefts` TEXT DEFAULT NULL,
    `companyDescription` text DEFAULT NULL,
    `description` text DEFAULT NULL,
    `instructions` TEXT DEFAULT NULL,
    `location` TEXT DEFAULT NULL,
    `rewards` TEXT DEFAULT NULL,
    `picture` TEXT DEFAULT NULL,
    `idCreator` INT DEFAULT NULL
);


CREATE TABLE `productTesting`(
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `productType` TEXT DEFAULT NULL,
  `feedback` TEXT DEFAULT NULL,
  `testStatus` TEXT DEFAULT NULL,
  `dateOfReception` TIMESTAMP DEFAULT current_timestamp()
);

CREATE TABLE `surveyQuestions`(
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `content` TEXT DEFAULT NULL,
  `creatorId` INT DEFAULT NULL,
  `testStatus` TEXT DEFAULT NULL
);

CREATE TABLE `surveyAnswer`(
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `content` TEXT DEFAULT NULL,
  `userId` INT DEFAULT NULL,
  `questionId` INT DEFAULT NULL,
  `testStatus` TEXT DEFAULT NULL
);


CREATE TABLE `dataRequest`(
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `creatorId` INT DEFAULT NULL,
  `geolocation` TEXT DEFAULT NULL,
  `timeSpendingOnCalls` TEXT DEFAULT NULL,
  `country` TEXT DEFAULT NULL
);

CREATE TABLE `paymentinformation` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `linkedWallet` text DEFAULT NULL,
  `linkedSecundaryWallet` text DEFAULT NULL,
  `linkedBankAccountName` text DEFAULT NULL,
  `linkedBankAccountNumber` INT DEFAULT NULL
);

CREATE TABLE `user`(
  `username` TEXT NOT NULL,
  `password` TEXT NOT NULL,
  `role` TEXT NOT NULL DEFAULT "user",
  `token` TEXT NOT NULL
)

CREATE TABLE `profile` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
    `name` TEXT NOT NULL,
    `nickname` TEXT NOT NULL,
    `lastName` TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `address` TEXT NOT NULL,
    `state` TEXT NOT NULL,
    `postCode` TEXT NOT NULL,
    `phoneNumber` TEXT NOT NULL,
    `country` TEXT NOT NULL,
);

CREATE TABLE `profileQuestion`(
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `questionName` TEXT DEFAULT NULL,
  `questionGroup` TEXT DEFAULT NULL,
  `questionGroupDisplay` TEXT DEFAULT NULL,
  `questionDescription` TEXT DEFAULT NULL,
  `questionType` TEXT DEFAULT NULL,
  `answerOptionId` INT DEFAULT NULL,
  `additionalComents` TEXT DEFAULT NULL,
  `sysActive` TINYINT(1) DEFAULT NULL
);

CREATE TABLE `profileAnswer`(
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `answerName` TEXT DEFAULT NULL,
  `answerGroup` TEXT DEFAULT NULL,
  `answerGroupDisplay` TEXT DEFAULT NULL,
  `answerDescription` TEXT DEFAULT NULL,
  `answerType` TEXT DEFAULT NULL,
  `answerOptionId` INT DEFAULT null,
  `additionalComents` TEXT DEFAULT NULL,
  `sysActive` TINYINT(1) DEFAULT NULL
);

CREATE TABLE `profileUserDetail`(
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `questionId` INT DEFAULT NULL,
  `answerId` INT DEFAULT NULL,
  `userId` INT DEFAULT NULL
);