-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-10-2022 a las 04:26:40
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `datamarket`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datarequest`
--

CREATE TABLE `datarequest` (
  `id` int(11) NOT NULL,
  `creatorId` int(11) DEFAULT NULL,
  `geolocation` text DEFAULT NULL,
  `timeSpendingOnCalls` text DEFAULT NULL,
  `country` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `offers`
--

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paymentinformation`
--

CREATE TABLE `paymentinformation` (
  `id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `linkedWallet` text DEFAULT NULL,
  `linkedSecundaryWallet` text DEFAULT NULL,
  `linkedBankAccountName` text DEFAULT NULL,
  `linkedBankAccountNumber` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producttesting`
--

CREATE TABLE `producttesting` (
  `id` int(11) NOT NULL,
  `productType` text DEFAULT NULL,
  `feedback` text DEFAULT NULL,
  `testStatus` text DEFAULT NULL,
  `dateOfReception` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profile`
--

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

--
-- Volcado de datos para la tabla `profile`
--

INSERT INTO `profile` (`id`, `created_at`, `name`, `nickname`, `lastName`, `email`, `address`, `state`, `postCode`, `phoneNumber`, `country`, `userId`, `isVerified`) VALUES
(1, '2022-10-22 02:00:41', 'Matias', '', '', 'pepito@gmail.com', '', '', '', '', '', NULL, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profileanswer`
--

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profilequestion`
--

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

--
-- Volcado de datos para la tabla `profilequestion`
--

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profileuserdetail`
--

CREATE TABLE `profileuserdetail` (
  `id` int(11) NOT NULL,
  `questionId` int(11) DEFAULT NULL,
  `answerId` int(11) DEFAULT NULL,
  `userId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `surveyanswer`
--

CREATE TABLE `surveyanswer` (
  `id` int(11) NOT NULL,
  `content` text DEFAULT NULL,
  `userId` int(11) DEFAULT NULL,
  `questionId` int(11) DEFAULT NULL,
  `testStatus` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `surveyquestions`
--

CREATE TABLE `surveyquestions` (
  `id` int(11) NOT NULL,
  `content` text DEFAULT NULL,
  `creatorId` int(11) DEFAULT NULL,
  `testStatus` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `role` text NOT NULL DEFAULT 'user',
  `token` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`, `token`) VALUES
(1, 'Matias', 'lala1234', 'user', '');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `datarequest`
--
ALTER TABLE `datarequest`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `offers`
--
ALTER TABLE `offers`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `paymentinformation`
--
ALTER TABLE `paymentinformation`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `producttesting`
--
ALTER TABLE `producttesting`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userId` (`userId`);

--
-- Indices de la tabla `profileanswer`
--
ALTER TABLE `profileanswer`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `profilequestion`
--
ALTER TABLE `profilequestion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `profileuserdetail`
--
ALTER TABLE `profileuserdetail`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `surveyanswer`
--
ALTER TABLE `surveyanswer`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `surveyquestions`
--
ALTER TABLE `surveyquestions`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `datarequest`
--
ALTER TABLE `datarequest`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `offers`
--
ALTER TABLE `offers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `paymentinformation`
--
ALTER TABLE `paymentinformation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `producttesting`
--
ALTER TABLE `producttesting`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `profile`
--
ALTER TABLE `profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `profileanswer`
--
ALTER TABLE `profileanswer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `profilequestion`
--
ALTER TABLE `profilequestion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `profileuserdetail`
--
ALTER TABLE `profileuserdetail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `surveyanswer`
--
ALTER TABLE `surveyanswer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `surveyquestions`
--
ALTER TABLE `surveyquestions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `profile`
--
ALTER TABLE `profile`
  ADD CONSTRAINT `profile_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
