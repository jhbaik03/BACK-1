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
-- Table structure for table `match_result`
--

DROP TABLE IF EXISTS `match_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match_result` (
  `matchID` int NOT NULL AUTO_INCREMENT,
  `blueTeamName` varchar(45) DEFAULT NULL,
  `blueTopChampion` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `blueTopKill` int DEFAULT NULL,
  `blueTopDeath` int DEFAULT NULL,
  `blueTopAssist` int DEFAULT NULL,
  `blueJglChampion` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `blueJglKill` int DEFAULT NULL,
  `blueJglDeath` int DEFAULT NULL,
  `blueJglAssist` int DEFAULT NULL,
  `blueMidChampion` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `blueMidKill` int DEFAULT NULL,
  `blueMidDeath` int DEFAULT NULL,
  `blueMidAssist` int DEFAULT NULL,
  `blueBtmChampion` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `blueBtmKill` int DEFAULT NULL,
  `blueBtmDeath` int DEFAULT NULL,
  `blueBtmAssist` int DEFAULT NULL,
  `blueSupChampion` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `blueSupKill` int DEFAULT NULL,
  `blueSupDeath` int DEFAULT NULL,
  `blueSupAssist` int DEFAULT NULL,
  `redTeamName` varchar(45) DEFAULT NULL,
  `redTopChampion` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `redTopKill` int DEFAULT NULL,
  `redTopDeath` int DEFAULT NULL,
  `redTopAssist` int DEFAULT NULL,
  `redJglChampion` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `redJglKill` int DEFAULT NULL,
  `redJglDeath` int DEFAULT NULL,
  `redJglAssist` int DEFAULT NULL,
  `redMidChampion` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `redMidKill` int DEFAULT NULL,
  `redMidDeath` int DEFAULT NULL,
  `redMidAssist` int DEFAULT NULL,
  `redBtmChampion` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `redBtmKill` int DEFAULT NULL,
  `redBtmDeath` int DEFAULT NULL,
  `redBtmAssist` int DEFAULT NULL,
  `redSupChampion` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `redSupKill` int DEFAULT NULL,
  `redSupDeath` int DEFAULT NULL,
  `redSupAssist` int DEFAULT NULL,
  `winTeamName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`matchID`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match_result`
--

LOCK TABLES `match_result` WRITE;
/*!40000 ALTER TABLE `match_result` DISABLE KEYS */;
INSERT INTO `match_result` VALUES (49,'T1','NuNu',9,4,4,'Gragas',4,8,2,'Braum',4,4,8,'Olaf',5,5,2,'Zyra',6,3,4,'Gen','MasterYi',7,5,2,'Syndra',1,4,5,'Soraka',8,5,3,'Xerath',6,9,2,'Seraphine',6,8,8,'T1'),(50,'T1','MasterYi',6,4,7,'NuNu',9,0,6,'Sivir',4,6,8,'Singed',9,0,6,'Kaisa',4,3,5,'Gen','Annie',4,2,7,'Ashe',8,9,0,'Alistar',8,6,5,'RekSai',4,6,7,'Sylas',8,9,9,'T1'),(51,'T1','Gnar',1,1,1,'Nidalee',1,1,1,'Ryze',1,1,1,'Renekton',1,1,1,'Lulu',1,1,1,'Gen','NuNu',1,1,1,'Draven',1,1,1,'Renata',1,1,1,'Lucian',1,1,1,'Lillia',1,1,1,'T1'),(52,'T1','NuNu',4,3,6,'Galio',8,5,4,'Gnar',6,4,3,'Rakan',5,7,8,'Renekton',5,4,6,'KT','Ryze',9,8,7,'Graves',7,7,5,'Sylas',3,7,8,'Draven',5,4,6,'Renata',7,3,5,'T1'),(53,'KDF','Kayle',8,7,6,'Qiyana',5,4,3,'Trundle',2,2,1,'Kaisa',2,3,4,'Pyke',7,8,9,'T1','Kayn',0,7,6,'Kled',4,7,5,'Taliyah',3,4,7,'Teemo',8,9,5,'Heimerdinger',6,8,9,'T1');
/*!40000 ALTER TABLE `match_result` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-17 15:56:19
