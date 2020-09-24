-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 23, 2020 at 09:05 AM
-- Server version: 8.0.13-4
-- PHP Version: 7.2.24-0ubuntu0.18.04.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `QxKi8MQlUR`
--

-- --------------------------------------------------------

--
-- Table structure for table `DXB_DEP`
--

CREATE TABLE `TEMP_TABLE` (
  `FLIGHT_NO` char(4) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ORIGIN` varchar(4) COLLATE utf8_unicode_ci DEFAULT NULL,
  `DESTINATION` varchar(4) COLLATE utf8_unicode_ci DEFAULT NULL,
  `DEPATURE_TIME` time DEFAULT NULL,
  `ARRIVAL_TIME` time DEFAULT NULL,
  `DAY` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `TYPE` char(4) COLLATE utf8_unicode_ci DEFAULT NULL,
  `DURATION` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `DXB_DEP`
--


COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
