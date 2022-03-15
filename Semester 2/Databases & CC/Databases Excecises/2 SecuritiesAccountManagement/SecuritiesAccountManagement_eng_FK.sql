-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server Version:               10.5.4-MariaDB - mariadb.org binary distribution
-- Server Betriebssystem:        Win64
-- HeidiSQL Version:             10.1.0.5464
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Exportiere Datenbank Struktur für securitiesaccountmanagement
CREATE DATABASE IF NOT EXISTS `securitiesaccountmanagement` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `securitiesaccountmanagement`;

-- Exportiere Struktur von Tabelle securitiesaccountmanagement.account
CREATE TABLE IF NOT EXISTS `account` (
  `Account_id` int(11) NOT NULL DEFAULT 0,
  `Customer_id` int(11) DEFAULT 0,
  `Bank_id` int(11) DEFAULT 0,
  PRIMARY KEY (`Account_id`),
  KEY `FKcid` (`Customer_id`),
  KEY `FKbid` (`Bank_id`),
  CONSTRAINT `FKbid` FOREIGN KEY (`Bank_id`) REFERENCES `bank` (`Bank_id`),
  CONSTRAINT `FKcid` FOREIGN KEY (`Customer_id`) REFERENCES `customer` (`Customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle securitiesaccountmanagement.account: ~4 rows (ungefähr)
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` (`Account_id`, `Customer_id`, `Bank_id`) VALUES
	(1, 1, 50070010),
	(2, 2, 10010010),
	(3, 1, 50080000),
	(4, 3, 70120400);
/*!40000 ALTER TABLE `account` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle securitiesaccountmanagement.bank
CREATE TABLE IF NOT EXISTS `bank` (
  `Bank_id` int(11) NOT NULL DEFAULT 0,
  `Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Bank_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle securitiesaccountmanagement.bank: ~6 rows (ungefähr)
/*!40000 ALTER TABLE `bank` DISABLE KEYS */;
INSERT INTO `bank` (`Bank_id`, `Name`) VALUES
	(10010010, 'POSTBANK BERLIN'),
	(20050550, 'HAMBURGER SPARKASSE'),
	(50040000, 'COMMERZBANK FRANKFURT'),
	(50070010, 'DEUTSCHE BANK FRANKFURT'),
	(50080000, 'DRESDNER BANK FRANKFURT'),
	(70120400, 'DIREKT ANLAGE BANK MUENCHEN');
/*!40000 ALTER TABLE `bank` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle securitiesaccountmanagement.customer
CREATE TABLE IF NOT EXISTS `customer` (
  `Customer_id` int(11) NOT NULL DEFAULT 0,
  `Name` varchar(50) DEFAULT NULL,
  `Address` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`Customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle securitiesaccountmanagement.customer: ~4 rows (ungefähr)
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` (`Customer_id`, `Name`, `Address`) VALUES
	(1, 'Müller, Erich', 'Kleistweg 9, 63892 Frankfurt'),
	(2, 'Schmidt, Beate', 'Reitgasse 10, 35037 Marburg'),
	(3, 'Meier, Thomas', 'Talstraße 106, 56243 Hintertupfing'),
	(4, 'Kaiser, Eva', 'Torstraße 12, 63452 Frankfurt');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle securitiesaccountmanagement.item
CREATE TABLE IF NOT EXISTS `item` (
  `Account_id` int(11) DEFAULT 0,
  `Purchase_date` datetime DEFAULT NULL,
  `Security_id` int(11) DEFAULT 0,
  `Number` int(11) DEFAULT 0,
  `Purchase_price` float DEFAULT 0,
  KEY `FKsid` (`Security_id`),
  KEY `FKaid` (`Account_id`),
  CONSTRAINT `FKaid` FOREIGN KEY (`Account_id`) REFERENCES `account` (`Account_id`),
  CONSTRAINT `FKsid` FOREIGN KEY (`Security_id`) REFERENCES `security` (`Security_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle securitiesaccountmanagement.item: ~12 rows (ungefähr)
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` (`Account_id`, `Purchase_date`, `Security_id`, `Number`, `Purchase_price`) VALUES
	(1, '1999-06-10 00:00:00', 575800, 20, 60),
	(1, '1999-06-10 00:00:00', 515100, 10, 70),
	(1, '1999-11-26 00:00:00', 716463, 5, 700),
	(1, '1999-11-26 00:00:00', 695200, 10, 550),
	(2, '1999-06-10 00:00:00', 604843, 15, 120),
	(2, '1999-11-26 00:00:00', 802000, 17, 68),
	(2, '1999-11-26 00:00:00', 823212, 20, 35),
	(3, '1999-10-12 00:00:00', 550000, 10, 175),
	(3, '1999-11-26 00:00:00', 656000, 10, 1250),
	(3, '1999-11-26 00:00:00', 766400, 8, 1500),
	(4, '1999-11-26 00:00:00', 843002, 100, 770),
	(4, '1999-11-26 00:00:00', 648300, 100, 1300);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle securitiesaccountmanagement.security
CREATE TABLE IF NOT EXISTS `security` (
  `Security_id` int(11) NOT NULL DEFAULT 0,
  `Name` varchar(50) DEFAULT NULL,
  `Price` float DEFAULT 0,
  PRIMARY KEY (`Security_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle securitiesaccountmanagement.security: ~30 rows (ungefähr)
/*!40000 ALTER TABLE `security` DISABLE KEYS */;
INSERT INTO `security` (`Security_id`, `Name`, `Price`) VALUES
	(515100, 'BASF', 82.25),
	(519000, 'Bayerische Motoren-Werke ST', 1704.1),
	(550000, 'Daimler-Benz', 170),
	(551200, 'Degussa', 105.3),
	(555700, 'Deutsche Telekom', 40.4),
	(575200, 'Bayer', 84.6),
	(575800, 'Hoechst', 72.45),
	(593700, 'MAN ST', 616),
	(604843, 'Henkel KGaA VZ', 134.4),
	(627500, 'Karstadt', 722),
	(648300, 'Linde', 1342),
	(656000, 'Mannesmann', 1354),
	(695200, 'PREUSSAG', 630.5),
	(703700, 'RWE ST', 99.5),
	(716463, 'SAP VZ', 782.5),
	(717200, 'Schering', 217.8),
	(723600, 'Siemens', 123.8),
	(725750, 'METRO ST', 81.5),
	(748500, 'Thyssen', 397.5),
	(761440, 'VEBA', 131.2),
	(762620, 'VIAG', 1008),
	(766400, 'Volkswagen ST', 1448),
	(802000, 'Bayerische Hypotheken- u. Wechselbank', 101),
	(802200, 'Bayerische Vereinsbank', 135),
	(803200, 'Commerzbank', 66.8),
	(804010, 'Deutsche Bank', 139.15),
	(804610, 'Dresdner Bank', 84.2),
	(823212, 'Deutsche Lufthansa vNA', 38.95),
	(840400, 'Allianz vNA', 558.5),
	(843002, 'Münchener Rückversicherung NA', 800);
/*!40000 ALTER TABLE `security` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
