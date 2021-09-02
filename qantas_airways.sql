-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 03, 2021 at 12:52 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qantas_airways`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `srnum` int(11) NOT NULL,
  `custid` varchar(200) DEFAULT NULL,
  `flightcode` varchar(200) DEFAULT NULL,
  `halal_meat` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`srnum`, `custid`, `flightcode`, `halal_meat`) VALUES
(12, 'HAR12', 'CAN12', 'y'),
(14, 'Gur009', 'CAN12', 'y');

-- --------------------------------------------------------

--
-- Table structure for table `clients`
--

CREATE TABLE `clients` (
  `clientcode` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `pincode` varchar(200) NOT NULL,
  `street` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `state` varchar(200) NOT NULL,
  `country` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `clients`
--

INSERT INTO `clients` (`clientcode`, `name`, `email`, `phone`, `pincode`, `street`, `city`, `state`, `country`) VALUES
('Gur009', 'Gurpreet Singh', 'gurpreet@gmail.com', '9129182012', '1290890', 'Street 2 Village Rasulpur', 'Rupnagar', 'Punjab', 'India'),
('HAR12', 'Harmanjot Singh', 'singhharmanjot2k2@gmail.com', '8528295675', '140001', '433 Giani Zail Singh Nagar', 'Ropar', 'Punjab', 'India'),
('JAS05', 'Jashanjot Singh', 'jashan@gmail.com', '9876718928', '140001', '433 Giani Zail Singh Nagar', 'Rupnagar', 'Punjab', 'India');

-- --------------------------------------------------------

--
-- Table structure for table `flights`
--

CREATE TABLE `flights` (
  `flightcode` varchar(100) NOT NULL,
  `origin` varchar(100) NOT NULL,
  `origintime` varchar(100) DEFAULT NULL,
  `destination` varchar(255) NOT NULL,
  `depttime` varchar(100) DEFAULT NULL,
  `luggage` varchar(255) DEFAULT NULL,
  `totalseats` int(11) NOT NULL,
  `filledup` int(11) NOT NULL,
  `free` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flights`
--

INSERT INTO `flights` (`flightcode`, `origin`, `origintime`, `destination`, `depttime`, `luggage`, `totalseats`, `filledup`, `free`) VALUES
('CAN12', 'IND', '09:56:28', 'YYZ Toronto', '15:56:28', '23+23+7', 200, 2, 198);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`srnum`),
  ADD KEY `custid` (`custid`),
  ADD KEY `flightcode` (`flightcode`);

--
-- Indexes for table `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`clientcode`);

--
-- Indexes for table `flights`
--
ALTER TABLE `flights`
  ADD PRIMARY KEY (`flightcode`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `srnum` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`custid`) REFERENCES `clients` (`clientcode`),
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`flightcode`) REFERENCES `flights` (`flightcode`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
