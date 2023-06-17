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
-- Table structure for table `match_ban`
--

DROP TABLE IF EXISTS `match_ban`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match_ban` (
  `matchID` int NOT NULL,
  `blueteam_ban1` varchar(45) DEFAULT NULL,
  `blueteam_ban2` varchar(45) DEFAULT NULL,
  `blueteam_ban3` varchar(45) DEFAULT NULL,
  `blueteam_ban4` varchar(45) DEFAULT NULL,
  `blueteam_ban5` varchar(45) DEFAULT NULL,
  `redteam_ban1` varchar(45) DEFAULT NULL,
  `redteam_ban2` varchar(45) DEFAULT NULL,
  `redteam_ban3` varchar(45) DEFAULT NULL,
  `redteam_ban4` varchar(45) DEFAULT NULL,
  `redteam_ban5` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`matchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match_ban`
--

LOCK TABLES `match_ban` WRITE;
/*!40000 ALTER TABLE `match_ban` DISABLE KEYS */;
INSERT INTO `match_ban` VALUES (50,'Morgana','Azir','Sion','Lucian','Cassiopeia','Soraka','Sona','Warwick','DrMundo','Samira'),(52,'Garen','LeBlanc','Neeko','Nami','RekSai','Lux','Nasus','Nautilus','Nilah','Rell'),(53,'Camille','Taric','KogMaw','Kindred','Fiora','AurelionSol','Amumu','Ahri','Thresh','Singed');
/*!40000 ALTER TABLE `match_ban` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-17 15:56:20
