-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 25, 2019 at 06:23 PM
-- Server version: 10.1.25-MariaDB
-- PHP Version: 7.1.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flightdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `fbooktab`
--

CREATE TABLE `fbooktab` (
  `BookID` varchar(20) NOT NULL,
  `FlightID` varchar(20) NOT NULL,
  `BDate` date NOT NULL,
  `JourneyDate` date NOT NULL,
  `Seats` int(11) NOT NULL,
  `CustID` varchar(20) NOT NULL,
  `CustName` varchar(20) NOT NULL,
  `Status` varchar(10) NOT NULL DEFAULT 'Confirm'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fbooktab`
--

INSERT INTO `fbooktab` (`BookID`, `FlightID`, `BDate`, `JourneyDate`, `Seats`, `CustID`, `CustName`, `Status`) VALUES
('B1095_JP_DLE', 'F001_JP_DLE', '0000-00-00', '2019-01-29', 2, 'xxx', 'Amit', 'Confirm'),
('B3042_JP_DLE', 'F001_JP_DLE', '0000-00-00', '2019-01-29', 2, 'sadf', 'fgdfg', 'Confirm'),
('B4520_JP_DLE', 'F001_JP_DLE', '2019-01-23', '2019-01-27', 1, 'C341', 'Ritu', 'Confirm'),
('B4521_JP_DLE', 'F002_JP_MB', '2019-01-24', '2019-01-28', 2, 'C456', 'Shruti', 'Confirm');

-- --------------------------------------------------------

--
-- Table structure for table `flightreg`
--

CREATE TABLE `flightreg` (
  `FlightID` varchar(30) NOT NULL,
  `FBoard` varchar(50) NOT NULL,
  `FDest` varchar(50) NOT NULL,
  `SeatCap` int(11) NOT NULL,
  `Schedule` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `flightreg`
--

INSERT INTO `flightreg` (`FlightID`, `FBoard`, `FDest`, `SeatCap`, `Schedule`) VALUES
('asdf', 'bgbf', 'dfd', 34, 'Dep:9  Arr:11'),
('F001_JP_DLE', 'Jaipur', 'Delhi', 6, 'Dep: 11:30  Arrival:13:15'),
('F002_JP_MB', 'Jaipur', 'Mumbai', 5, 'Dep: 16:30  Arrival:18:00'),
('F002_JP_PN', 'Jaipur', 'Pune', 4, 'Dep: 10:00  Arrival:11:30'),
('F004_DLE_JP', 'Delhi', 'Jaipur', 5, 'Dep: 11:30  Arrival:13:15'),
('F005_PN_JP', 'Pune', 'Jaipur', 7, 'Dep: 11:30  Arrival:13:15'),
('F007_JP_DLE', 'Jaipur', 'Delhi', 5, 'Dep: 16:00  Arrival:17:00'),
('F008_JP_DLE', 'Jaipur', 'Delhi', 10, 'Dep: 22:00  Arrival:23:00');

-- --------------------------------------------------------

--
-- Stand-in structure for view `seatstatus`
-- (See below for the actual view)
--
CREATE TABLE `seatstatus` (
`FlightID` varchar(20)
,`JourneyDate` date
,`sumOfSeats` decimal(32,0)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `seatsummary`
-- (See below for the actual view)
--
CREATE TABLE `seatsummary` (
`FlightID` varchar(30)
,`FBoard` varchar(50)
,`FDest` varchar(50)
,`SeatCap` int(11)
,`JourneyDate` date
,`AvSeats` decimal(33,0)
);

-- --------------------------------------------------------

--
-- Structure for view `seatstatus`
--
DROP TABLE IF EXISTS `seatstatus`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `seatstatus`  AS  select `fbooktab`.`FlightID` AS `FlightID`,`fbooktab`.`JourneyDate` AS `JourneyDate`,sum(`fbooktab`.`Seats`) AS `sumOfSeats` from `fbooktab` group by `fbooktab`.`FlightID`,`fbooktab`.`JourneyDate` ;

-- --------------------------------------------------------

--
-- Structure for view `seatsummary`
--
DROP TABLE IF EXISTS `seatsummary`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `seatsummary`  AS  select `flightreg`.`FlightID` AS `FlightID`,`flightreg`.`FBoard` AS `FBoard`,`flightreg`.`FDest` AS `FDest`,`flightreg`.`SeatCap` AS `SeatCap`,`seatstatus`.`JourneyDate` AS `JourneyDate`,(`flightreg`.`SeatCap` - ifnull(`seatstatus`.`sumOfSeats`,0)) AS `AvSeats` from (`flightreg` left join `seatstatus` on((`flightreg`.`FlightID` = `seatstatus`.`FlightID`))) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fbooktab`
--
ALTER TABLE `fbooktab`
  ADD PRIMARY KEY (`BookID`);

--
-- Indexes for table `flightreg`
--
ALTER TABLE `flightreg`
  ADD PRIMARY KEY (`FlightID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
