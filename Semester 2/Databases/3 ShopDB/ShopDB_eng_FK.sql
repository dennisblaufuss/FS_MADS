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


-- Exportiere Datenbank Struktur für shopdb
CREATE DATABASE IF NOT EXISTS `shopdb` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `shopdb`;

-- Exportiere Struktur von Tabelle shopdb.customer
CREATE TABLE IF NOT EXISTS `customer` (
  `Customer_id` int(11) NOT NULL,
  `Lastname` varchar(20) DEFAULT NULL,
  `Firstname` varchar(20) DEFAULT NULL,
  `Address` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`Customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle shopdb.customer: ~8 rows (ungefähr)
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` (`Customer_id`, `Lastname`, `Firstname`, `Address`) VALUES
	(1, 'Meier', 'Egon', 'Cappeler Str. 3, 35043 Marburg'),
	(2, 'Schmidt', 'Bettina', 'Biegenstr. 12, 35037 Marburg'),
	(3, 'Behring AG', '', 'Sonnenallee 1, 35039 Marburg'),
	(4, 'Weber', 'Markus', 'Marktplatz 4, 36235 Gladenbach'),
	(5, 'Tille', 'Verena', 'Am Born 24, 36233 Biedenkopf'),
	(6, 'Kahler', 'Robert', 'Schwanallee 37, 35037 Marburg'),
	(7, 'Wald GmbH', '', 'Industriepark 7, 34562 Allendorf'),
	(8, 'Meier KG', '', 'Parkstr. 2, 35055 Moischt');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle shopdb.item
CREATE TABLE IF NOT EXISTS `item` (
  `Order_id` int(11) DEFAULT NULL,
  `Product_id` int(11) DEFAULT NULL,
  `Number` int(11) DEFAULT NULL,
  KEY `FKoid` (`Order_id`),
  KEY `FKpid` (`Product_id`),
  CONSTRAINT `FKoid` FOREIGN KEY (`Order_id`) REFERENCES `orders` (`Order_id`),
  CONSTRAINT `FKpid` FOREIGN KEY (`Product_id`) REFERENCES `product` (`Product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle shopdb.item: ~24 rows (ungefähr)
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` (`Order_id`, `Product_id`, `Number`) VALUES
	(1, 2, 1),
	(1, 5, 1),
	(1, 8, 1),
	(1, 10, 1),
	(1, 13, 1),
	(1, 14, 1),
	(1, 15, 1),
	(2, 15, 3),
	(3, 3, 15),
	(3, 7, 8),
	(4, 13, 1),
	(5, 9, 2),
	(5, 4, 1),
	(6, 1, 4),
	(6, 12, 6),
	(7, 5, 1),
	(8, 11, 3),
	(9, 6, 18),
	(9, 14, 30),
	(10, 8, 4),
	(11, 12, 7),
	(12, 7, 3),
	(13, 13, 12),
	(13, 4, 10);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle shopdb.orders
CREATE TABLE IF NOT EXISTS `orders` (
  `Order_id` int(11) NOT NULL,
  `Customer_id` int(11) DEFAULT NULL,
  `Order_date` varchar(9) DEFAULT NULL,
  PRIMARY KEY (`Order_id`),
  KEY `FKcid` (`Customer_id`),
  CONSTRAINT `FKcid` FOREIGN KEY (`Customer_id`) REFERENCES `customer` (`Customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle shopdb.orders: ~13 rows (ungefähr)
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` (`Order_id`, `Customer_id`, `Order_date`) VALUES
	(1, 1, '01/02/96'),
	(2, 2, '01/02/96'),
	(3, 3, '11/02/96'),
	(4, 4, '04/03/96'),
	(5, 1, '06/03/96'),
	(6, 3, '13/03/96'),
	(7, 5, '07/05/96'),
	(8, 6, '07/05/96'),
	(9, 7, '10/05/96'),
	(10, 3, '10/05/96'),
	(11, 8, '14/05/96'),
	(12, 3, '21/07/96'),
	(13, 8, '23/07/96');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle shopdb.product
CREATE TABLE IF NOT EXISTS `product` (
  `Product_id` int(11) NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Price` float DEFAULT NULL,
  `Supplier_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Product_id`),
  KEY `FKsid` (`Supplier_id`),
  CONSTRAINT `FKsid` FOREIGN KEY (`Supplier_id`) REFERENCES `supplier` (`Supplier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle shopdb.product: ~15 rows (ungefähr)
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` (`Product_id`, `Name`, `Price`, `Supplier_id`) VALUES
	(1, 'Monitor 14"', 450, 1),
	(2, 'Monitor 15"', 625, 1),
	(3, 'Monitor 17"', 990, 3),
	(4, 'Monitor 21"', 1300, 4),
	(5, 'Festplatte 1GB', 250, 2),
	(6, 'Festplatte 2GB', 320, 3),
	(7, 'Festplatte 3GB', 350, 2),
	(8, 'Gehaeuse Mini', 50, 1),
	(9, 'Gehaeuse Tower', 70, 1),
	(10, 'Board 133MHz', 600, 4),
	(11, 'Board 166MHz', 820, 4),
	(12, 'Board 200MHz', 1130, 3),
	(13, 'Graphikkarte', 250, 2),
	(14, 'Tastatur', 78, 1),
	(15, 'RAM 16MB', 150, 2);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle shopdb.supplier
CREATE TABLE IF NOT EXISTS `supplier` (
  `Supplier_id` int(11) NOT NULL,
  `Name` varchar(80) DEFAULT NULL,
  `Address` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`Supplier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Exportiere Daten aus Tabelle shopdb.supplier: ~4 rows (ungefähr)
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` (`Supplier_id`, `Name`, `Address`) VALUES
	(1, 'Benteler AG', 'Hohlweg 29, 26253 Paderborn'),
	(2, 'Metzler GmbH', 'Am Platz 3, 64385 Jena'),
	(3, 'Gruber KG', 'Hochstr. 13, 73653 Bad Vilbel'),
	(4, 'Sesam AG', 'Bachstr. 63, 53424 Kassel');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
