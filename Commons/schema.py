instructions = [
    'SET FOREIGN_KEY_CHECKS=0',
    'DROP TABLE IF EXISTS offers;',
    'DROP TABLE IF EXISTS users;',
    'DROP TABLE IF EXISTS surveys;',
    'SET FOREIGN_KEY_CHECKS=1',
    """
            CREATE TABLE `datarequest` (
            `id` int(11) NOT NULL,
            `creatorId` int(11) DEFAULT NULL,
            `geolocation` text DEFAULT NULL,
            `timeSpendingOnCalls` text DEFAULT NULL,
            `country` text DEFAULT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """,
    """
        CREATE TABLE `offers` (
        `id` int(11) NOT NULL,
        `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
        `companyName` text DEFAULT NULL,
        `offerTitle` text DEFAULT NULL,
        `industry` text DEFAULT NULL,
        `type` text DEFAULT NULL,
        `verification` tinyint(1) DEFAULT 1,
        `reviews` text DEFAULT NULL,
        `appliedUsers` text DEFAULT NULL,
        `offersAvailables` text DEFAULT NULL,
        `offersLefts` text DEFAULT NULL,
        `companyDescription` text DEFAULT NULL,
        `description` text DEFAULT NULL,
        `instructions` text DEFAULT NULL,
        `location` text DEFAULT NULL,
        `rewards` text DEFAULT NULL,
        `picture` text DEFAULT NULL,
        `idCreator` int(11) DEFAULT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """,
    """
        CREATE TABLE `paymentinformation` (
        `id` int(11) NOT NULL,
        `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
        `linkedWallet` text DEFAULT NULL,
        `linkedSecundaryWallet` text DEFAULT NULL,
        `linkedBankAccountName` text DEFAULT NULL,
        `linkedBankAccountNumber` int(11) DEFAULT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """,
    """
        CREATE TABLE `producttesting` (
        `id` int(11) NOT NULL,
        `productType` text DEFAULT NULL,
        `feedback` text DEFAULT NULL,
        `testStatus` text DEFAULT NULL,
        `dateOfReception` timestamp NOT NULL DEFAULT current_timestamp()
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """,
    """
        CREATE TABLE `profile` (
        `id` int(11) NOT NULL,
        `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
        `name` text NOT NULL,
        `nickname` text NOT NULL,
        `lastName` text NOT NULL,
        `email` text NOT NULL,
        `address` text NOT NULL,
        `state` text NOT NULL,
        `postCode` text NOT NULL,
        `phoneNumber` text NOT NULL,
        `country` text NOT NULL,
        `userId` int(11) DEFAULT NULL,
        `isVerified` tinyint(1) NOT NULL DEFAULT 0
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """,
    """
        INSERT INTO `profile` (`id`, `created_at`, `name`, `nickname`, `lastName`, `email`, `address`, `state`, `postCode`, `phoneNumber`, `country`, `userId`, `isVerified`) VALUES
        (1, '2022-10-22 02:00:41', 'Matias', '', '', 'pepito@gmail.com', '', '', '', '', '', NULL, 0);
    """,
    """
        CREATE TABLE `profileanswer` (
        `id` int(11) NOT NULL,
        `answerName` text DEFAULT NULL,
        `answerGroup` text DEFAULT NULL,
        `answerGroupDisplay` text DEFAULT NULL,
        `answerDescription` text DEFAULT NULL,
        `answerType` text DEFAULT NULL,
        `answerOptionId` int(11) DEFAULT NULL,
        `additionalComents` text DEFAULT NULL,
        `sysActive` tinyint(1) DEFAULT 1
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """,
    """
        INSERT INTO `profileanswer` (`id`, `answerName`, `answerGroup`, `answerGroupDisplay`, `answerDescription`, `answerType`, `answerOptionId`, `additionalComents`, `sysActive`) VALUES
        (1, 'user entry string', 'user entry', 'null', 'please enter your answer', 'user entry string', 1, '', 1),
        (2, 'user entry integer', 'user entry', 'null', 'please enter your answer - must contain number without letters or special characters', 'user entry integer', 2, '', 1),
        (3, 'user entry date', 'user entry', 'dd/mm/yyyy', 'please enter your date of birth -format must by dd/mm/yyyy', 'user entry date', 3, '', 1),
        (4, 'multiple choice -yes', 'multiple choice bool', 'Yes', 'yes, if you do', 'multiple choice', 4, '', 1),
        (5, 'multiple choice -no', 'multiple choice bool', 'No', 'No, if you do not', 'multiple choice', 4, '', 1),
        (6, 'multiple choice -Male', 'multiple choice bool', 'MALE', 'MALE', 'multiple choice', 5, '', 1),
        (7, 'multiple choice -Female', 'multiple choice bool', 'FEMALE', 'FEMALE', 'multiple choice', 5, '', 1),
        (8, 'multiple choice -NON BINARY', 'multiple choice bool', 'NON-BINARY', 'NON-BINARY', 'multiple choice', 5, '', 1),
        (9, 'Full time work', 'multiple choice multiple', 'Full time work', 'work 8 hours or more', 'multiple choice', 6, '', 1),
        (10, 'Part time work', 'multiple choice bool', 'Part time or casual work', 'less than 8 hours daily', 'multiple choice', 6, '', 1),
        (11, 'Casual, seasonal or temporary work', 'multiple choice bool', 'Casual, seasonal or temporary work', 'Casual work or seasonal', 'multiple choice', 6, '', 1),
        (12, 'Full time student', 'multiple choice bool', 'Full time student', 'unemployed full time student', 'multiple choice', 6, '', 1),
        (14, 'Part time student', 'multiple choice bool', 'Part time student', 'Part time student', 'multiple choice', 6, '', 1),
        (15, 'Domestic home duties', 'multiple choice bool', 'Domestic home duties', NULL, 'multiple choice', 6, '', 1),
        (16, 'Retired', 'multiple choice bool', 'Retired', NULL, 'multiple choice', 6, '', 1),
        (17, 'Unemployed', 'multiple choice bool', 'Unemployed', NULL, 'multiple choice', 6, '', 1),
        (18, 'Other (please describe below)', 'multiple choice bool', 'Other (please describe below)', NULL, 'multiple choice', 6, '', 1),
        (19, 'Accept term and conditions', 'multiple choice bool', 'I have read, and agree to the Terms of service', NULL, 'multiple choice', 7, '', 1);
    """,
    """
        CREATE TABLE `profilequestion` (
        `id` int(11) NOT NULL,
        `questionName` text DEFAULT NULL,
        `questionGroup` text DEFAULT NULL,
        `questionGroupDisplay` text DEFAULT NULL,
        `questionDescription` text DEFAULT NULL,
        `questionType` text DEFAULT NULL,
        `answerOptionId` int(11) DEFAULT NULL,
        `additionalComents` text DEFAULT NULL,
        `sysActive` tinyint(1) DEFAULT 1
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """,
    """
        INSERT INTO `profilequestion` (`id`, `questionName`, `questionGroup`, `questionGroupDisplay`, `questionDescription`, `questionType`, `answerOptionId`, `additionalComents`, `sysActive`) VALUES
        (1, 'Name', 'name', '1. What is your name?', 'please enter your name and details exactly as they appear on your ID or Doc used to vefiry your identity', 'user entry', 1, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (2, 'Last Name', 'name', '1. What is your name?', 'please enter your name and details exactly as they appear on your ID or Doc used to vefiry your identity', 'user entry', 1, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (3, 'gender', 'gender', '3. What\'s your gender?', 'define your gender will help us to find relevants offers for you', 'Multiple choice', 4, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (4, 'date of birth', 'age/date of birth', '4. What\'s your date of birth?', 'please enter your name and details exactly as they appear on your ID or Doc used to vefiry your identity', 'user entry', 3, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (5, 'date of birth', 'age/date of birth', '4. What\'s your date of birth?', 'Day', 'user entry', 2, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (6, 'date of birth', 'age/date of birth', '4. What\'s your date of birth?', 'Month', 'user entry', 2, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (7, 'date of birth', 'age/date of birth', '4. What\'s your date of birth?', 'Year', 'user entry', 2, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (9, 'Country', 'address', '5. What is your address?', 'enter your country', 'user entry', 1, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (10, 'State/Province', 'address', '5. What is your address?', 'enter your state or province of residence', 'user entry', 1, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (11, 'Postcode', 'address', '5. What is your address?', 'enter your postcode', 'user entry', 1, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (12, 'Street name', 'address', '5. What is your address?', 'enter your street name or rd name', 'user entry', 1, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (13, 'Street number', 'address', '5. What is your address?', 'enter your street number', 'user entry', 2, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (14, 'Apartment/Flat/Unit number (if any)', 'address', '5. What is your address?', 'enter your flat or apartment number', 'user entry', 1, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (15, 'Additional residence information', 'address', '5. What is your address?', 'any additional information if needed', 'user entry', 1, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (16, 'Occupation status', 'Occupation', '6.What best describes your current occupation status?', 'You may select two options  or more options if relevant', 'user entry', 1, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (17, 'phone and contact verification', 'contact', '7. What\'s your mobile phone number?', 'please enter your phone number without country code', 'user entry', 2, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1),
        (18, 'phone verification', 'contact', 'Enter the verification code sent to your phone', 'enter the code to complete the sign in proccess', 'user entry', 2, 'This is part of the user validation', 1),
        (19, 'term and conditions', 'term and conditions', 'Please read the term and conditions before continue', 'Please read the term and conditions before continue', 'Multiple choice', 0, '', 0),
        (20, 'sport_main', 'sports', '2. Do you exercise regularly?', 'please enter yes or no', 'Multiple choice', 4, 'This won\'t be displayed publicly we only use this to match you with the perfect offers for you', 1);
    """
]