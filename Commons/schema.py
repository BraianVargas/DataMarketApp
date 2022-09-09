instructions = [
    'SET FOREIGN_KEY_CHECKS=0',
    'DROP TABLE IF EXISTS offers;',
    'DROP TABLE IF EXISTS users;',
    'DROP TABLE IF EXISTS surveys;',
    'SET FOREIGN_KEY_CHECKS=1',
    """
    CREATE TABLE offers (
        offerId INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        companyName VARCHAR(50),
        offerTitle VARCHAR(50),
        industry VARCHAR(50),
        type VARCHAR(50),
        verification BOOLEAN,
        reviews VARCHAR(50),
        appliedUsers VARCHAR(50),
        offersAvailables VARCHAR(50),
        offersLefts VARCHAR(50),
        companyDescription TEXT,
        description TEXT,
        instructions VARCHAR(50),
        location VARCHAR(50),
        rewards VARCHAR(50),
        picture VARCHAR(50)
        );
    """,
    """
    CREATE TABLE user (
        userId INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        name VARCHAR(50) NOT NULL,
        nickname VARCHAR(50) NOT NULL,
        lastName VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        address VARCHAR(50) NOT NULL,
        state VARCHAR(50) NOT NULL,
        postCode VARCHAR(50) NOT NULL,
        phoneNumber VARCHAR(50) NOT NULL,
        country VARCHAR(50) NOT NULL,
        password VARCHAR(255) NOT NULL
        );
    """,
    """
    CREATE TABLE paymentInformation (
        id INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        linkedWallet TEXT,
        linkedSecundaryWallet TEXT,
        linkedBankAccountName TEXT,
        linkedBankAccountNumber INT
    );
    """

]


# """
# CREATE TABLE surveys (
#    PREGUNTAR DATOS SURVEYS
# );
# """,