-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 10, 2020 at 02:18 PM
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
-- Table structure for table `BOOKINGS`
--

CREATE TABLE `BOOKINGS` (
  `CUSTOMER_ID` int(11) NOT NULL,
  `BOOKING_ID` int(11) NOT NULL,
  `DEPATURE_DATE` int(11) NOT NULL,
  `DEPATURE_TIME` int(11) NOT NULL,
  `SEAT_NO` int(11) NOT NULL,
  `AMOUNT (USD)` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `CUSTOMERS`
--

CREATE TABLE `CUSTOMERS` (
  `CUSTOMER_ID` int(11) NOT NULL,
  `CUSTOMER_NAME` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `CUSTOMER_PHONE` int(20) NOT NULL,
  `CUSTOMER_EMAIL` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `CUSTOMER_SEX` char(3) COLLATE utf8_unicode_ci NOT NULL,
  `CUSTOMER_DOB` date NOT NULL,
  `CUSTOMER_NATIONALITY` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `CUSTOMER_PASSPORT_NUMBER` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `PASSPORT`
--

CREATE TABLE `PASSPORT` (
  `CUSTOMER_ID` int(11) NOT NULL,
  `P_NUMBER` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `P_NAME` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `P_EXPIRY` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ROUTES`
--

CREATE TABLE `ROUTES` (
  `FLIGHT_NO` varchar(4) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `ORIGIN` varchar(4) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `DESTINATION` varchar(4) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `DEPATURE_TIME` time DEFAULT NULL,
  `ARRIVAL_TIME` time DEFAULT NULL,
  `DAY` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `TYPE` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `DURATION` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `ROUTES`
--

INSERT INTO `ROUTES` (`FLIGHT_NO`, `ORIGIN`, `DESTINATION`, `DEPATURE_TIME`, `ARRIVAL_TIME`, `DAY`, `TYPE`, `DURATION`) VALUES
('G615', 'DXB', 'BOM', '07:00:00', '10:15:00', 'DAILY', 'DIR', '03:15:00'),
('G615', 'BOM', 'DXB', '11:30:00', '14:45:00', 'DAILY', 'DIR', '03:15:00'),
('G725', 'DXB', 'SYD', '07:00:00', '20:45:00', 'SUN/TUES/THUR', 'DIR', '13:45:00'),
('G725', 'SYD', 'DXB', '22:00:00', '11:45:00', 'SUN/TUES/THUR', 'DIR', '13:45:00'),
('G799', 'DXB', 'BOM', '12:00:00', '15:15:00', 'MON/WED/FRI', 'CON', '03:15:00'),
('G799', 'BOM', 'SYD', '16:30:00', '04:00:00', 'MON/WED/FRI', 'CON', '12:00:00'),
('G799', 'SYD', 'BOM', '05:15:00', '17:15:00', 'TUES/THUR/SAT', 'CON', '12:00:00'),
('G799', 'BOM', 'DXB', '18:30:00', '21:45:00', 'TUES/THURS/SAT', 'CON', '03:15:00'),
('G219', 'DXB', 'LHR', '05:00:00', '13:10:00', 'DAILY', 'DIR', '08:10:00'),
('G219', 'LHR', 'DXB', '14:25:00', '22:35:00', 'DAILY', 'DIR', '08:10:00'),
('G125', 'DXB', 'JFK', '02:00:00', '15:00:00', 'SUN/TUES/THUR', 'DIR', '13:00:00'),
('G125', 'JFK', 'DXB', '16:15:00', '05:15:00', 'SUN/TUES/THUR', 'DIR', '13:00:00'),
('G756', 'DXB', 'LHR', '08:00:00', '16:10:00', 'MON/WED/FRI', 'CON', '08:10:00'),
('G756', 'LHR', 'JFK', '17:25:00', '01:25:00', 'MON/WED/FRI', 'CON', '08:00:00'),
('G756', 'JFK', 'LHR', '02:40:00', '10:40:00', 'TUES/THUR/SAT', 'CON', '08:00:00'),
('G756', 'LHR', 'DXB', '11:55:00', '20:05:00', 'TUES/THUR/SAT', 'CON', '08:10:00'),
('G559', 'DXB', 'BOM', '15:30:00', '18:45:00', 'DAILY', 'DIR', '03:15:00'),
('G559', 'BOM', 'DXB', '22:00:00', '01:15:00', 'DAILY', 'DIR', '03:15:00'),
('G310', 'DXB', 'SYD', '00:00:00', '13:45:00', 'MON/WED/FRI', 'DIR', '13:45:00'),
('G310', 'SYD', 'DXB', '15:00:00', '04:45:00', 'MON/WED/FRI', 'DIR', '13:45:00'),
('G281', 'DXB', 'BOM', '20:00:00', '23:15:00', 'MON/WED/SAT', 'CON', '03:15:00'),
('G281', 'BOM', 'SYD', '00:30:00', '12:30:00', 'SUN/TUES/THUR', 'CON', '12:00:00'),
('G281', 'SYD', 'BOM', '13:45:00', '01:45:00', 'SUN/TUES/THUR', 'CON', '12:00:00'),
('G281', 'BOM', 'DXB', '03:45:00', '07:00:00', 'SUN/TUES/THUR', 'CON', '03:15:00'),
('G993', 'DXB', 'LHR', '15:00:00', '23:10:00', 'DAILY', 'DIR', '08:10:00'),
('G993', 'LHR', 'DXB', '00:30:00', '08:40:00', 'DAILY', 'DIR', '08:00:00'),
('G635', 'DXB', 'JFK', '12:00:00', '01:55:00', 'MON/WED/FRI', 'DIR', '13:00:00'),
('G635', 'JFK', 'DXB', '03:10:00', '19:10:00', 'TUES/THUR/SAT', 'DIR', '13:00:00'),
('G498', 'DXB', 'LHR', '23:00:00', '07:00:00', 'SUN/TUES/THUR', 'CON', '08:10:00'),
('G498', 'LHR', 'JFK', '08:15:00', '16:15:00', 'MON/WED/FRI', 'CON', '08:00:00'),
('G498', 'JFK', 'LHR', '17:30:00', '01:30:00', 'MON/WED/FRI', 'CON', '08:00:00'),
('G498', 'LHR', 'DXB', '02:45:00', '10:55:00', 'TUES/THUR/SAT', 'CON', '08:10:00');

-- --------------------------------------------------------

--
-- Table structure for table `SCHEDULE`
--

CREATE TABLE `SCHEDULE` (
  `FLIGHT_NO` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ORIGIN` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `DESTINATION` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `DEPATURE_TIME` time DEFAULT NULL,
  `ARRIVAL_TIME` time DEFAULT NULL,
  `DURATION` int(2) DEFAULT NULL,
  `DAYS OF OPERATION` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `SEAT_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `BOOKINGS`
--
ALTER TABLE `BOOKINGS`
  ADD PRIMARY KEY (`BOOKING_ID`);

--
-- Indexes for table `CUSTOMERS`
--
ALTER TABLE `CUSTOMERS`
  ADD PRIMARY KEY (`CUSTOMER_ID`);

--
-- Indexes for table `SCHEDULE`
--
ALTER TABLE `SCHEDULE`
  ADD UNIQUE KEY `SEAT_ID` (`SEAT_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
