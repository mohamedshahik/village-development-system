-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 05, 2024 at 09:08 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1villagepydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `complainttb`
--

CREATE TABLE `complainttb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Department` varchar(250) NOT NULL,
  `Info` varchar(500) NOT NULL,
  `Image` varchar(500) NOT NULL,
  `Action` varchar(500) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `OfficerName` varchar(250) NOT NULL,
  `CImage` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `complainttb`
--

INSERT INTO `complainttb` (`id`, `UserName`, `Mobile`, `Department`, `Info`, `Image`, `Action`, `Status`, `OfficerName`, `CImage`) VALUES
(1, 'san', '9486365535', 'Roads And Transportation', 'path hole Problem', '5820.png', 'Problem Solved', 'Completed', 'san123', ''),
(2, 'arun', '9600357839', 'Drinking Water Facilities', 'waterere', '9914.png', '', 'waiting', '', ''),
(3, 'parveen', '9500935840', 'Roads And Transportation', 'crack', '4800.png', 'complated', 'Completed', 'san123', '5485.png');

-- --------------------------------------------------------

--
-- Table structure for table `officertb`
--

CREATE TABLE `officertb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `Department` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `officertb`
--

INSERT INTO `officertb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `Department`, `UserName`, `Password`) VALUES
(1, 'sangeeth', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'Roads And Transportation', 'san123', 'san123'),
(2, 'arun', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'Drinking Water Facilities', 'arun', 'arun');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'sangeeth', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san'),
(2, 'arun', '9600357839', 'arun@gmail.com', 'no 6 trichy', 'arun', 'arun'),
(3, 'parveen', '9500935840', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'parveen', 'parveen');
