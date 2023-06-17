-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: back
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player` (
  `Player_ID` int unsigned NOT NULL,
  `Player_Name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `Position` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `Main` tinyint(1) NOT NULL,
  PRIMARY KEY (`Player_ID`),
  UNIQUE KEY `Player ID_UNIQUE` (`Player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
INSERT INTO `player` VALUES (1,'Zeus','TOP',0),(2,'Oner','JGL',0),(3,'Faker','MID',0),(4,'Skyyy','MID',1),(5,'Gumayusi','BOT',0),(6,'Keria','SPT',0),(7,'Doran','TOP',0),(8,'Peanut','JGL',0),(9,'Chovy','MID',0),(10,'Peyz','BOT',0),(11,'Delight','SPT',0),(12,'Kiin','TOP',0),(13,'Cuzz','JGL',0),(14,'Bdd','MID',0),(15,'Aiming','BOT',0),(16,'Lehends','SPT',0),(17,'Canna','TOP',0),(18,'Canyon','JGL',0),(19,'ShowMaker','MID',0),(20,'Deft','BOT',0),(21,'Kellin','SPT',0),(22,'Kingen','TOP',0),(23,'Clid','JGL',0),(24,'ZEKA','MID',0),(25,'Viper','BOT',0),(26,'Life','SPT',0),(27,'Burdol','TOP',0),(28,'Willer','JGL',0),(29,'Clozer','MID',0),(30,'Teddy','BOT',0),(31,'Kael','SPT',0),(32,'DuDu','TOP',0),(33,'YoungJae','JGL',0),(34,'BuLLDoG','MID',0),(35,'Taeyoon','BOT',0),(36,'Jun','SPT',0),(37,'Moham','SPT',1),(38,'Morgan','TOP',0),(39,'UmTi','JGL',0),(40,'Raptor','JGL',1),(41,'Karis','MID',0),(42,'Hena','BOT',0),(43,'Effort','SPT',0),(44,'Rascal','TOP',0),(45,'Croco','JGL',0),(46,'Juhan','JGL',1),(47,'FATE','MID',0),(48,'deokdam','BOT',0),(49,'Pleata','BOT',1),(50,'BeryL','SPT',0),(51,'DnDn','TOP',0),(52,'Sylvie','JGL',0),(53,'FIESTA','MID',0),(54,'Callme','MID',1),(55,'vital','BOT',0),(56,'Peter','SPT',0);
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-17 15:56:21
