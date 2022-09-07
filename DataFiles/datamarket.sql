
CREATE TABLE `offers` (
  `offerId` int(11) NOT NULL,
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
  `picture` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `offers`
--

INSERT INTO `offers` (`offerId`, `created_at`, `companyName`, `offerTitle`, `industry`, `type`, `verification`, `reviews`, `appliedUsers`, `offersAvailables`, `offersLefts`, `companyDescription`, `description`, `instructions`, `location`, `rewards`, `picture`) VALUES
(1, '0000-00-00 00:00:00', 'Captus Ltd', 'Kombucha tropical flavors', 'beverages/softdrink manufacturing', 'Product testing & Survey', 0, '4.5', '800', '80', '20', 'Authentic kombucha fermented with no shortcuts', 'We are looking for great people with passion about eating healthy and wellbing. We are developing a range of new tropical flavors for our kombucha, becuase Healthy could be testy as well. So, do yourselft and your gut a favor  + boost your immute system and help us to develop and explore these amazing flavors', 'when you click in Apply and  accept this offer you', 'Sydney-Australia', '0', ''),
(2, '0000-00-00 00:00:00', 'Captus Ltd', 'Kombucha tropical flavors', 'beverages/softdrink manufacturing', 'Product testing & Survey', 0, '4.5', '800', '80', '20', 'Authentic kombucha fermented with no shortcuts', 'We are looking for great people with passion about eating healthy and wellbing. We are developing a range of new tropical flavors for our kombucha, becuase Healthy could be testy as well. So, do yourselft and your gut a favor  + boost your immute system and help us to develop and explore these amazing flavors', 'when you click in Apply and  accept this offer you', 'Sydney-Australia', '0', ''),
(3, '0000-00-00 00:00:00', 'Captus Ltd', 'Kombucha tropical flavors', 'beverages/softdrink manufacturing', 'Product testing & Survey', 0, '4.5', '800', '80', '20', 'Authentic kombucha fermented with no shortcuts', 'We are looking for great people with passion about eating healthy and wellbing. We are developing a range of new tropical flavors for our kombucha, becuase Healthy could be testy as well. So, do yourselft and your gut a favor  + boost your immute system and help us to develop and explore these amazing flavors', 'when you click in Apply and  accept this offer you', 'Sydney-Australia', '0', ''),
(4, '0000-00-00 00:00:00', 'Captus Ltd', 'Kombucha tropical flavors', 'beverages/softdrink manufacturing', 'Product testing & Survey', 0, '4.5', '800', '80', '20', 'Authentic kombucha fermented with no shortcuts', 'We are looking for great people with passion about eating healthy and wellbing. We are developing a range of new tropical flavors for our kombucha, becuase Healthy could be testy as well. So, do yourselft and your gut a favor  + boost your immute system and help us to develop and explore these amazing flavors', 'when you click in Apply and  accept this offer you', 'Sydney-Australia', '0', ''),
(145, '0000-00-00 00:00:00', 'Lab', 'Laboratory Trials', 'healthcare and health technology', 'Product testing & Survey', 0, '', '', '', '', '', '', '', '', '', '');

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
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `userId` int(11) NOT NULL,
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
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `offers`
--
ALTER TABLE `offers`
  ADD PRIMARY KEY (`offerId`);

--
-- Indices de la tabla `paymentinformation`
--
ALTER TABLE `paymentinformation`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userId`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `offers`
--
ALTER TABLE `offers`
  MODIFY `offerId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=146;

--
-- AUTO_INCREMENT de la tabla `paymentinformation`
--
ALTER TABLE `paymentinformation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `userId` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
