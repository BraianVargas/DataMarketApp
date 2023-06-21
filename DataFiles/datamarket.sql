-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-10-2022 a las 04:32:31
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

--
-- Volcado de datos para la tabla `profileanswer`
--

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

INSERT INTO `profilequestion`(`questionName`, `questionGroup`, `questionDescription`, `questionType`, `additionalComents`, `sysActive`)
VALUES
(`Personal Details -Name`, `Last Name`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Personal Details -Name`, `Names`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Personal Details`, `Male`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `Multiple choice`, `comments`, 1),
(`Personal Details`, `Female`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `Multiple choice`, `comments`, 1),
(`Personal Details`, `Non-Binary`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `Multiple choice`, `comments`, 1),
(`Personal Details`, `Day`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Personal Details`, `Month`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Personal Details`, `Year`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Personal Details`, `Nationality`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Personal identity validation`, `ID number`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Where do you live?`, `Country`, `What is your address?`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Where do you live?`, `State/Province`, `What is your address?`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Where do you live?`, `Postcode`, `What is your address?`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Where do you live?`, `Street`, `What is your address?`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Where do you live?`, `Street name`, `What is your address?`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Where do you live?`, `Street number`, `What is your address?`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Where do you live?`, `Apartment/Flat/Unit number (if any)`, `What is your address?`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Contact details`, `Mobile/cell`, `What is your mobile phone number`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1),
(`Contact details`, `email`, `Email`, `This will not be shared or displayed publicaly, we onle use this to show you suitable offers`, `User Entry`, `comments`, 1);
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
  `role` text NOT NULL DEFAULT `user`,
  `token` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`, `token`) VALUES
(1, `Matias`, `lala1234`, `user`, ``);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

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
