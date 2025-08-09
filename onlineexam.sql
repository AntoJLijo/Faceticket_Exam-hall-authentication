-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 27, 2025 at 09:23 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `onlineexam`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`uname`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `atten`
--

CREATE TABLE `atten` (
  `id` int(10) NOT NULL auto_increment,
  `regno` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `atten`
--

INSERT INTO `atten` (`id`, `regno`, `date`, `status`) VALUES
(1, '7904461600', '2024-03-07', 'Absent');

-- --------------------------------------------------------

--
-- Table structure for table `college`
--

CREATE TABLE `college` (
  `id` int(10) NOT NULL auto_increment,
  `colname` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `colcode` varchar(100) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `college`
--


-- --------------------------------------------------------

--
-- Table structure for table `exam`
--

CREATE TABLE `exam` (
  `id` int(50) NOT NULL auto_increment,
  `etype` varchar(250) NOT NULL,
  `depart` varchar(250) NOT NULL,
  `year` varchar(250) NOT NULL,
  `sub` varchar(250) NOT NULL,
  `date` varchar(250) NOT NULL,
  `sess` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `exam`
--

INSERT INTO `exam` (`id`, `etype`, `depart`, `year`, `sub`, `date`, `sess`) VALUES
(1, 'model', 'mca', '1 Year', 'sample', '2020-12-25', 'FN'),
(2, 'model', 'mca', '1 Year', 'sample1', '2020-12-25', 'FN'),
(3, 'online q', 'mca', '1 Year', 'php', '2022-04-20', 'FN'),
(4, 'model', 'Mca', '1 Year', '234234', '2023-03-25', 'FN'),
(5, 'model', 'Mca', '1 Year', '234234', '2024-02-18', 'FN'),
(6, 'sem', 'computer', '1 Year', 'java', '2024-03-21', 'FN'),
(7, 'model', 'Mca', '1 Year', 'sample', '2024-04-18', 'FN');

-- --------------------------------------------------------

--
-- Table structure for table `hall1`
--

CREATE TABLE `hall1` (
  `id` int(50) NOT NULL auto_increment,
  `etype` varchar(250) NOT NULL,
  `regno` varchar(250) NOT NULL,
  `hno` varchar(250) NOT NULL,
  `sub` varchar(250) NOT NULL,
  `date` varchar(250) NOT NULL,
  `sess` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `hall1`
--

INSERT INTO `hall1` (`id`, `etype`, `regno`, `hno`, `sub`, `date`, `sess`) VALUES
(6, 'model', '812414104006', '1', 'sample', '2024-02-24', 'FN'),
(7, 'model', '1231', '12', 'sample', '2024-03-15', 'FN'),
(8, 'model', '321654', '12', 'sample', '2024-04-18', 'FN');

-- --------------------------------------------------------

--
-- Table structure for table `mark`
--

CREATE TABLE `mark` (
  `id` int(50) NOT NULL,
  `regno` varchar(50) NOT NULL,
  `etype` varchar(50) NOT NULL,
  `s1` varchar(50) NOT NULL,
  `m1` varchar(50) NOT NULL,
  `s2` varchar(50) NOT NULL,
  `m2` varchar(50) NOT NULL,
  `s3` varchar(50) NOT NULL,
  `m3` varchar(50) NOT NULL,
  `s4` varchar(50) NOT NULL,
  `m4` varchar(50) NOT NULL,
  `s5` varchar(50) NOT NULL,
  `m5` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mark`
--

INSERT INTO `mark` (`id`, `regno`, `etype`, `s1`, `m1`, `s2`, `m2`, `s3`, `m3`, `s4`, `m4`, `s5`, `m5`) VALUES
(0, '7904461600', 't1', 'asdfa12', '12', 't', '12', 'fasdf', '12', 'asdfasd', '12', 'asdfas', '12');

-- --------------------------------------------------------

--
-- Table structure for table `question1`
--

CREATE TABLE `question1` (
  `id` int(50) NOT NULL auto_increment,
  `qlevel` varchar(100) NOT NULL,
  `year` varchar(1000) NOT NULL,
  `depart` varchar(1000) NOT NULL,
  `etype` varchar(1000) NOT NULL,
  `name` varchar(1000) NOT NULL,
  `suint` varchar(1000) NOT NULL,
  `question` varchar(1000) NOT NULL,
  `ans1` varchar(1000) NOT NULL,
  `ans2` varchar(1000) NOT NULL,
  `ans3` varchar(1000) NOT NULL,
  `ans4` varchar(1000) NOT NULL,
  `ans` varchar(1000) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `question1`
--

INSERT INTO `question1` (`id`, `qlevel`, `year`, `depart`, `etype`, `name`, `suint`, `question`, `ans1`, `ans2`, `ans3`, `ans4`, `ans`) VALUES
(1, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', '1', '1', '1', '1', '1', '1'),
(2, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', '2', '2', '2', '2', '2', '2'),
(3, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', '3', '3', '3', '3', '3', '3'),
(4, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', '4', '4', '4', '4', '4', '4'),
(5, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', '5', '5', '5', '5', '5', '5'),
(6, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', '6', '6', '6', '6', '6', '6'),
(7, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', '7', '7', '7', '7', '7', '7'),
(8, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', 'sample test', 'q', 'w', 'e', 'q', 'q'),
(9, 'Easy', '1 Year', 'MCA', 'test', 'sample', 'test', 'test', 'test', 'test', 'test', 'test', 'test');

-- --------------------------------------------------------

--
-- Table structure for table `question2`
--

CREATE TABLE `question2` (
  `id` int(50) NOT NULL auto_increment,
  `qlevel` varchar(100) NOT NULL,
  `year` varchar(1000) NOT NULL,
  `depart` varchar(1000) NOT NULL,
  `etype` varchar(1000) NOT NULL,
  `name` varchar(1000) NOT NULL,
  `suint` varchar(1000) NOT NULL,
  `question` varchar(1000) NOT NULL,
  `mark` varchar(1000) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `question2`
--

INSERT INTO `question2` (`id`, `qlevel`, `year`, `depart`, `etype`, `name`, `suint`, `question`, `mark`) VALUES
(1, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', 'what?', '2'),
(2, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', 'test?', '2'),
(3, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', 'sample?', '2'),
(4, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', 'example?', '2'),
(5, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', 'testing?', '2'),
(6, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', 'sssssssss', '5'),
(7, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', 'ddddddd', '5'),
(8, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', 'tttttttttt', '5'),
(9, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', 'gggggggggg', '10'),
(10, 'Easy', '1 Year', 'MCA', 'test', 'sample', '', 'nnnnnnnnnnnnnnnn', '10');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id` int(50) NOT NULL auto_increment,
  `exam` varchar(250) NOT NULL,
  `subject` varchar(250) NOT NULL,
  `question` varchar(250) NOT NULL,
  `ans1` varchar(250) NOT NULL,
  `ans2` varchar(250) NOT NULL,
  `ans3` varchar(250) NOT NULL,
  `ans4` varchar(250) NOT NULL,
  `ans` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `questions`
--


-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(50) NOT NULL auto_increment,
  `studentid` varchar(250) NOT NULL,
  `name` varchar(250) NOT NULL,
  `gender` varchar(250) NOT NULL,
  `dob` varchar(250) NOT NULL,
  `depart` varchar(250) NOT NULL,
  `year` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `pnumber` varchar(250) NOT NULL,
  `address` varchar(250) NOT NULL,
  `sem` varchar(50) NOT NULL,
  `class1` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `studentid`, `name`, `gender`, `dob`, `depart`, `year`, `email`, `pnumber`, `address`, `sem`, `class1`) VALUES
(1, '1231', 'sundar', 'male', '2024-03-07', 'Mca', '1 Year', 'sundarv06@gmail.com', '7904461600', 'trichy', '1', 'a'),
(2, '225214317', 'Ragul M', 'male', '2002-04-23', 'computer science', '2 Year', 'ragulgokul94471@gmail.com', '6383645595', 'BHC', '4', 'c'),
(3, '2313123', 'sundar', 'male', '2024-03-29', 'computer', '1 Year', 'mani@gmail.com', '7904461601', 'trichy', '1', '1'),
(4, '321654', 'sundar', 'male', '2024-04-17', 'Mca', '1 Year', 'sundarv06@gmail.com', '7904461601', 'trichy', '1', 'a');

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

CREATE TABLE `result` (
  `id` int(50) NOT NULL auto_increment,
  `uid` varchar(250) NOT NULL,
  `name` varchar(250) NOT NULL,
  `qname` varchar(250) NOT NULL,
  `tques` varchar(250) NOT NULL,
  `result` varchar(250) NOT NULL,
  `status` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `result`
--

INSERT INTO `result` (`id`, `uid`, `name`, `qname`, `tques`, `result`, `status`) VALUES
(1, '1', '1', 'sample1', '10', '1', '1'),
(3, '1', '1', 'sample1', '10', '1', '1'),
(4, '1', '1', 'sample1', '10', '1', '1'),
(5, '1', '1', 'sample1', '10', '1', '1'),
(6, '1', '1', 'sample1', '10', '2', '1');

-- --------------------------------------------------------

--
-- Table structure for table `staffregister`
--

CREATE TABLE `staffregister` (
  `id` int(50) NOT NULL auto_increment,
  `staffid` varchar(250) NOT NULL,
  `name` varchar(250) NOT NULL,
  `gender` varchar(250) NOT NULL,
  `dob` varchar(250) NOT NULL,
  `depart` varchar(250) NOT NULL,
  `year` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `pnumber` varchar(250) NOT NULL,
  `address` varchar(250) NOT NULL,
  `sem` varchar(50) NOT NULL,
  `class1` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `staffregister`
--

INSERT INTO `staffregister` (`id`, `staffid`, `name`, `gender`, `dob`, `depart`, `year`, `email`, `pnumber`, `address`, `sem`, `class1`) VALUES
(1, '1234', 'sundar', 'male', '2020-12-12', 'mca', '2 Year', 'sundarv06@gmail.com', '7904461600', '24/d, fathima street, puthur, trichy-17', '1', 'a class'),
(2, '14789632', 'sundar', 'male', '2022-04-23', 'mca', '1 Year', 'sundarv06@gmail.com', '7904461600', 'trichy', '1 sem', 'a'),
(3, '1231', 'sam', 'male', '2023-02-15', 'Mca', '1 Year', 'sundarv06@gmail.com', '7904461600', 'trichy', '1', 'a'),
(4, '123456', 'pandiyan', 'male', '2023-02-25', 'Mca', '1 Year', 'sundarv06@gmail.com', '7904461600', 'trichy', '1', '123'),
(5, '1234567', 'sam', 'male', '2023-04-01', 'Mca', '1 Year', 'teset@gmail.com', '7904461600', 'trichy', '1', 'a'),
(6, '1231', 'sam', 'male', '2024-04-17', 'Mca', '1 Year', 'sundarv06@gmail.com', '7904461601', 'trichy', '1', 'a');

-- --------------------------------------------------------

--
-- Table structure for table `timetable`
--

CREATE TABLE `timetable` (
  `id` int(10) NOT NULL auto_increment,
  `year` varchar(50) NOT NULL,
  `depart` varchar(50) NOT NULL,
  `day` varchar(10) NOT NULL,
  `p1` varchar(50) NOT NULL,
  `p2` varchar(50) NOT NULL,
  `p3` varchar(50) NOT NULL,
  `p4` varchar(50) NOT NULL,
  `p5` varchar(50) NOT NULL,
  `sem` varchar(10) NOT NULL,
  `class` varchar(10) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `timetable`
--

INSERT INTO `timetable` (`id`, `year`, `depart`, `day`, `p1`, `p2`, `p3`, `p4`, `p5`, `sem`, `class`) VALUES
(1, '1Year', 'MSC', '1', 'ww', 'www', 'www', 'ww', 'www', '', ''),
(2, '1 Year', 'MCA', '2', 'ee', 'ee', 'ee', 'ee', 'ee', '', ''),
(3, '1 Year', 'MCA', '1', 'ts', 'ml', 'ms', 'ss', 'jj', '1', 'a');

-- --------------------------------------------------------

--
-- Table structure for table `updatestatus`
--

CREATE TABLE `updatestatus` (
  `id` int(10) NOT NULL auto_increment,
  `sid` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `updatestatus`
--

INSERT INTO `updatestatus` (`id`, `sid`, `status`) VALUES
(1, '1231', ''),
(2, '225214317', '');

-- --------------------------------------------------------

--
-- Table structure for table `uques`
--

CREATE TABLE `uques` (
  `id` int(50) NOT NULL auto_increment,
  `uid` varchar(50) NOT NULL,
  `q1` varchar(50) NOT NULL,
  `q2` varchar(50) NOT NULL,
  `q3` varchar(50) NOT NULL,
  `q4` varchar(50) NOT NULL,
  `q5` varchar(50) NOT NULL,
  `q6` varchar(50) NOT NULL,
  `q7` varchar(50) NOT NULL,
  `q8` varchar(50) NOT NULL,
  `q9` varchar(50) NOT NULL,
  `q10` varchar(50) NOT NULL,
  `a1` varchar(50) NOT NULL,
  `a2` varchar(50) NOT NULL,
  `a3` varchar(50) NOT NULL,
  `a4` varchar(50) NOT NULL,
  `a5` varchar(50) NOT NULL,
  `a6` varchar(50) NOT NULL,
  `a7` varchar(50) NOT NULL,
  `a8` varchar(50) NOT NULL,
  `a9` varchar(50) NOT NULL,
  `a10` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `uques`
--

INSERT INTO `uques` (`id`, `uid`, `q1`, `q2`, `q3`, `q4`, `q5`, `q6`, `q7`, `q8`, `q9`, `q10`, `a1`, `a2`, `a3`, `a4`, `a5`, `a6`, `a7`, `a8`, `a9`, `a10`) VALUES
(1, '1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Tuesday', '61', '67000', '18', '1981709', '5', '9988', 'Bubble Memories', 'Digital Network Service', 'Novell'),
(2, '1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Tuesday', '61', '67000', '18', '1981709', '5', '9988', 'Bubble Memories', 'Digital Network Service', 'Novell'),
(3, '1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Tuesday', '61', '67000', '18', '1981709', '5', '9988', 'Bubble Memories', 'Digital Network Service', 'Novell'),
(4, '1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Sunday', '71', '76500', '21', '1981709', '5', '9988', 'Bubble Memories', 'Digital Network Service', 'Oracle'),
(5, '1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Tuesday', '61', '70000', '3', '1981709', '4', '9988', 'Floppy Disk', 'Domain Name System', 'Oracle');
