-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for delivery
CREATE DATABASE IF NOT EXISTS `delivery` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `delivery`;

-- Dumping structure for table delivery.delivery
CREATE TABLE IF NOT EXISTS `delivery` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tujuan` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `jarak` float NOT NULL,
  `notes` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `harga_delivery` int NOT NULL,
  `status` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `order_id` int NOT NULL,
  `member_id` int NOT NULL,
  `employee_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table delivery.delivery: ~4 rows (approximately)
REPLACE INTO `delivery` (`id`, `tujuan`, `jarak`, `notes`, `harga_delivery`, `status`, `order_id`, `member_id`, `employee_id`) VALUES
	(1, 'Jakarta', 320.5, 'kirim cepat', 160250, 'pending', 1, 3, NULL),
	(2, 'sby', 30.5, 'kirim cepat', 15250, 'pending', 2, 5, NULL),
	(3, 'malang', 10, 'kirim cepat', 5000, 'pending', 1, 3, NULL),
	(4, 'solo', 200, 'kirim cepat', 100000, 'pending', 3, 3, NULL),
	(5, 'solo', 200, 'kirim cepat', 100000, 'pending', 2, 1, NULL);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
