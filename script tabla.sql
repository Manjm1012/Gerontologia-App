CREATE DATABASE  IF NOT EXISTS `Gerontologia` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Gerontologia`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: Gerontologia
-- ------------------------------------------------------
-- Server version	9.1.0

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=193 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_adversidades`
--

DROP TABLE IF EXISTS `myapp_adversidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_adversidades` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `alergia_medicamento` tinyint(1) NOT NULL,
  `nombre_alergia_medicamento` varchar(255) NOT NULL,
  `autoprescripcion` tinyint(1) NOT NULL,
  `nombre_autoprescripcion` varchar(255) NOT NULL,
  `alergia_alimento` tinyint(1) NOT NULL,
  `nombre_alergia_alimento` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_alteracionsentidos`
--

DROP TABLE IF EXISTS `myapp_alteracionsentidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_alteracionsentidos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cataratas` tinyint(1) NOT NULL,
  `ceguera` tinyint(1) NOT NULL,
  `glaucoma` tinyint(1) NOT NULL,
  `presbiacusia` tinyint(1) NOT NULL,
  `otra_alteracion_sentidos` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_antecedentestoxicos`
--

DROP TABLE IF EXISTS `myapp_antecedentestoxicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_antecedentestoxicos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `alcohol` tinyint(1) NOT NULL,
  `frecuencia_alcohol` varchar(255) NOT NULL,
  `cigarrillo` tinyint(1) NOT NULL,
  `frecuencia_cigarrillo` varchar(255) NOT NULL,
  `cafe` tinyint(1) NOT NULL,
  `frecuencia_cafe` varchar(255) NOT NULL,
  `sustancia_psicoactiva` tinyint(1) NOT NULL,
  `frecuencia_sustancia` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_aspectosfisicos`
--

DROP TABLE IF EXISTS `myapp_aspectosfisicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_aspectosfisicos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `estado_fisico` varchar(2) NOT NULL,
  `condicion_malo` longtext,
  `fk_adversidades_id` bigint NOT NULL,
  `fk_antecedentes_toxicos_id` bigint NOT NULL,
  `fk_medicamentos_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fk_adversidades_id` (`fk_adversidades_id`),
  UNIQUE KEY `fk_antecedentes_toxicos_id` (`fk_antecedentes_toxicos_id`),
  KEY `myapp_aspectosfisico_fk_medicamentos_id_94a65d26_fk_myapp_med` (`fk_medicamentos_id`),
  CONSTRAINT `myapp_aspectosfisico_fk_adversidades_id_35a9f72e_fk_myapp_adv` FOREIGN KEY (`fk_adversidades_id`) REFERENCES `myapp_adversidades` (`id`),
  CONSTRAINT `myapp_aspectosfisico_fk_antecedentes_toxi_9562e999_fk_myapp_ant` FOREIGN KEY (`fk_antecedentes_toxicos_id`) REFERENCES `myapp_antecedentestoxicos` (`id`),
  CONSTRAINT `myapp_aspectosfisico_fk_medicamentos_id_94a65d26_fk_myapp_med` FOREIGN KEY (`fk_medicamentos_id`) REFERENCES `myapp_medicamentos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_aspectosfuncionales`
--

DROP TABLE IF EXISTS `myapp_aspectosfuncionales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_aspectosfuncionales` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `observacion_aspectos_funcionales` longtext,
  `fk_ayudas_ortopedicas_id` bigint NOT NULL,
  `fk_indice_KATZ_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fk_ayudas_ortopedicas_id` (`fk_ayudas_ortopedicas_id`),
  UNIQUE KEY `fk_indice_KATZ_id` (`fk_indice_KATZ_id`),
  CONSTRAINT `myapp_aspectosfuncio_fk_ayudas_ortopedica_353c6f45_fk_myapp_ayu` FOREIGN KEY (`fk_ayudas_ortopedicas_id`) REFERENCES `myapp_ayudasortopedicas` (`id`),
  CONSTRAINT `myapp_aspectosfuncio_fk_indice_KATZ_id_37b6de4f_fk_myapp_ind` FOREIGN KEY (`fk_indice_KATZ_id`) REFERENCES `myapp_indicekatz` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_aspectospsicogerontologicos`
--

DROP TABLE IF EXISTS `myapp_aspectospsicogerontologicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_aspectospsicogerontologicos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fk_depresiones_yasavage_id` bigint NOT NULL,
  `fk_enfermedades_mentales_id` bigint NOT NULL,
  `fk_valoraciones_mentales_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fk_depresiones_yasavage_id` (`fk_depresiones_yasavage_id`),
  UNIQUE KEY `fk_enfermedades_mentales_id` (`fk_enfermedades_mentales_id`),
  UNIQUE KEY `fk_valoraciones_mentales_id` (`fk_valoraciones_mentales_id`),
  CONSTRAINT `myapp_aspectospsicog_fk_depresiones_yasav_5199a2c4_fk_myapp_dep` FOREIGN KEY (`fk_depresiones_yasavage_id`) REFERENCES `myapp_depresionesyasavage` (`id`),
  CONSTRAINT `myapp_aspectospsicog_fk_enfermedades_ment_f90e5ebf_fk_myapp_enf` FOREIGN KEY (`fk_enfermedades_mentales_id`) REFERENCES `myapp_enfermedadesmentales` (`id`),
  CONSTRAINT `myapp_aspectospsicog_fk_valoraciones_ment_b57d3919_fk_myapp_val` FOREIGN KEY (`fk_valoraciones_mentales_id`) REFERENCES `myapp_valoracionesmentales` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_ayudasortopedicas`
--

DROP TABLE IF EXISTS `myapp_ayudasortopedicas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_ayudasortopedicas` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `caminador` tinyint(1) NOT NULL,
  `muletas` tinyint(1) NOT NULL,
  `silla_ruedas` tinyint(1) NOT NULL,
  `baston` tinyint(1) NOT NULL,
  `gafas` tinyint(1) NOT NULL,
  `audifonos` tinyint(1) NOT NULL,
  `protesis` tinyint(1) NOT NULL,
  `otra_ayuda_ortopedica` varchar(255) NOT NULL,
  `observacion_ayuda_ortopedica` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_ciudades`
--

DROP TABLE IF EXISTS `myapp_ciudades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_ciudades` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_ciudad` varchar(100) NOT NULL,
  `fk_departamento_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_ciudades_fk_departamento_id_1f4c73b9_fk_myapp_dep` (`fk_departamento_id`),
  CONSTRAINT `myapp_ciudades_fk_departamento_id_1f4c73b9_fk_myapp_dep` FOREIGN KEY (`fk_departamento_id`) REFERENCES `myapp_departamentos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_datossocioeconomicos`
--

DROP TABLE IF EXISTS `myapp_datossocioeconomicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_datossocioeconomicos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `actividad_desempeñada` varchar(255) NOT NULL,
  `actividad_actual` varchar(255) NOT NULL,
  `tipo_ingreso` varchar(255) NOT NULL,
  `valor_mensual_promedio` double NOT NULL,
  `clasificacion_ingreso` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_departamentos`
--

DROP TABLE IF EXISTS `myapp_departamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_departamentos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_departamento` varchar(255) NOT NULL,
  `fk_pais_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_departamentos_fk_pais_id_f28548cc_fk_myapp_paises_id` (`fk_pais_id`),
  CONSTRAINT `myapp_departamentos_fk_pais_id_f28548cc_fk_myapp_paises_id` FOREIGN KEY (`fk_pais_id`) REFERENCES `myapp_paises` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_depresionesyasavage`
--

DROP TABLE IF EXISTS `myapp_depresionesyasavage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_depresionesyasavage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `vida_satisfactoria` tinyint(1) NOT NULL,
  `renuncia` tinyint(1) NOT NULL,
  `vacio` tinyint(1) NOT NULL,
  `aburrido` tinyint(1) NOT NULL,
  `optimista` tinyint(1) NOT NULL,
  `temor` tinyint(1) NOT NULL,
  `feliz` tinyint(1) NOT NULL,
  `desamparado` tinyint(1) NOT NULL,
  `quedarse_casa` tinyint(1) NOT NULL,
  `fallo_memoria` tinyint(1) NOT NULL,
  `vivir` tinyint(1) NOT NULL,
  `nuevo_proyecto` tinyint(1) NOT NULL,
  `energia` tinyint(1) NOT NULL,
  `angustia` tinyint(1) NOT NULL,
  `economia` tinyint(1) NOT NULL,
  `total_puntuacion_depresion` smallint NOT NULL,
  `resultado` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_enfermedadesmentales`
--

DROP TABLE IF EXISTS `myapp_enfermedadesmentales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_enfermedadesmentales` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `psicosis` tinyint(1) NOT NULL,
  `transtorno_ansiedad` tinyint(1) NOT NULL,
  `problema_intergeneracional` tinyint(1) NOT NULL,
  `duelo_patologico` tinyint(1) NOT NULL,
  `transtorno_afectivo_bipolar` tinyint(1) NOT NULL,
  `depresion` tinyint(1) NOT NULL,
  `ideas_suicidas` varchar(2) NOT NULL,
  `observacion_suicidio` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_espiritualidades`
--

DROP TABLE IF EXISTS `myapp_espiritualidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_espiritualidades` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pertenece_grupo_religioso` tinyint(1) NOT NULL,
  `nombre_religion` varchar(255) DEFAULT NULL,
  `actividad_espiritual` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_evaluaciones_bucales`
--

DROP TABLE IF EXISTS `myapp_evaluaciones_bucales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_evaluaciones_bucales` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `valoracion` varchar(255) DEFAULT NULL,
  `observacion` longtext NOT NULL,
  `criterio` varchar(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_evolucionesmensuales`
--

DROP TABLE IF EXISTS `myapp_evolucionesmensuales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_evolucionesmensuales` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `seguimiento` longtext NOT NULL,
  `fecha_evolucion` date NOT NULL,
  `fk_historias_gerontologicas_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_evolucionesmen_fk_historias_geronto_ce5c7238_fk_myapp_his` (`fk_historias_gerontologicas_id`),
  CONSTRAINT `myapp_evolucionesmen_fk_historias_geronto_ce5c7238_fk_myapp_his` FOREIGN KEY (`fk_historias_gerontologicas_id`) REFERENCES `myapp_historiasgerontologicas` (`numero_historia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_gradosescolaridad`
--

DROP TABLE IF EXISTS `myapp_gradosescolaridad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_gradosescolaridad` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `lee` tinyint(1) NOT NULL,
  `escribe` tinyint(1) NOT NULL,
  `tiene_primaria` tinyint(1) NOT NULL,
  `primaria_finalizada` tinyint(1) NOT NULL,
  `tiene_secundaria` tinyint(1) NOT NULL,
  `secundaria_finalizada` tinyint(1) NOT NULL,
  `tiene_tecnica` tinyint(1) NOT NULL,
  `nombre_tecnica` varchar(100) NOT NULL,
  `tiene_tecnologia` tinyint(1) NOT NULL,
  `nombre_tecnologia` varchar(100) NOT NULL,
  `tiene_pregrado` tinyint(1) NOT NULL,
  `nombre_pregrado` varchar(100) NOT NULL,
  `tiene_posgrado` tinyint(1) NOT NULL,
  `nombre_posgrado` varchar(100) NOT NULL,
  `otro_estudio` tinyint(1) NOT NULL,
  `nombre_otro_estudio` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_habitos`
--

DROP TABLE IF EXISTS `myapp_habitos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_habitos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `persona_activa` tinyint(1) NOT NULL,
  `nombre_actividad` varchar(255) DEFAULT NULL,
  `actividad_fisica` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_historiasgerontologicas`
--

DROP TABLE IF EXISTS `myapp_historiasgerontologicas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_historiasgerontologicas` (
  `numero_historia` int NOT NULL,
  `fecha_consulta` date NOT NULL,
  `fecha_elaboracion` date NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `fecha_egreso` date NOT NULL,
  `actividad_desempeñada` varchar(100) NOT NULL,
  `observaciones_historia_gerontologica` longtext NOT NULL,
  `motivo` varchar(1) NOT NULL,
  `fk_aspectos_fisicos_id` bigint NOT NULL,
  `fk_aspectos_funcionales_id` bigint NOT NULL,
  `fk_aspectos_psicogerontologicos_id` bigint NOT NULL,
  `fk_Empleados_id` bigint NOT NULL,
  `fk_relacion_familias_id` bigint NOT NULL,
  `fk_revision_sistemas_id` bigint NOT NULL,
  `fk_situaciones_gerontologicas_id` bigint NOT NULL,
  `fk_tipo_familias_id` bigint NOT NULL,
  `fk_tipo_protecciones_exequiales_id` bigint NOT NULL,
  `fk_valoraciones_gerontologicas_id` bigint NOT NULL,
  PRIMARY KEY (`numero_historia`),
  UNIQUE KEY `fk_aspectos_fisicos_id` (`fk_aspectos_fisicos_id`),
  UNIQUE KEY `fk_aspectos_funcionales_id` (`fk_aspectos_funcionales_id`),
  UNIQUE KEY `fk_aspectos_psicogerontologicos_id` (`fk_aspectos_psicogerontologicos_id`),
  UNIQUE KEY `fk_relacion_familias_id` (`fk_relacion_familias_id`),
  UNIQUE KEY `fk_revision_sistemas_id` (`fk_revision_sistemas_id`),
  UNIQUE KEY `fk_situaciones_gerontologicas_id` (`fk_situaciones_gerontologicas_id`),
  UNIQUE KEY `fk_tipo_familias_id` (`fk_tipo_familias_id`),
  UNIQUE KEY `fk_tipo_protecciones_exequiales_id` (`fk_tipo_protecciones_exequiales_id`),
  UNIQUE KEY `fk_valoraciones_gerontologicas_id` (`fk_valoraciones_gerontologicas_id`),
  KEY `myapp_historiasgeron_fk_Empleados_id_397f26aa_fk_myapp_usu` (`fk_Empleados_id`),
  CONSTRAINT `myapp_historiasgeron_fk_aspectos_fisicos__0aad8c1f_fk_myapp_asp` FOREIGN KEY (`fk_aspectos_fisicos_id`) REFERENCES `myapp_aspectosfisicos` (`id`),
  CONSTRAINT `myapp_historiasgeron_fk_aspectos_funciona_2e321ede_fk_myapp_asp` FOREIGN KEY (`fk_aspectos_funcionales_id`) REFERENCES `myapp_aspectosfuncionales` (`id`),
  CONSTRAINT `myapp_historiasgeron_fk_aspectos_psicoger_ab7109dc_fk_myapp_asp` FOREIGN KEY (`fk_aspectos_psicogerontologicos_id`) REFERENCES `myapp_aspectospsicogerontologicos` (`id`),
  CONSTRAINT `myapp_historiasgeron_fk_relacion_familias_6c786e49_fk_myapp_rel` FOREIGN KEY (`fk_relacion_familias_id`) REFERENCES `myapp_relacionfamilias` (`id`),
  CONSTRAINT `myapp_historiasgeron_fk_revision_sistemas_45270bde_fk_myapp_rev` FOREIGN KEY (`fk_revision_sistemas_id`) REFERENCES `myapp_revisionsistemas` (`id`),
  CONSTRAINT `myapp_historiasgeron_fk_situaciones_geron_127acdcf_fk_myapp_sit` FOREIGN KEY (`fk_situaciones_gerontologicas_id`) REFERENCES `myapp_situacionesgerontologicas` (`id`),
  CONSTRAINT `myapp_historiasgeron_fk_tipo_familias_id_10c357cc_fk_myapp_tip` FOREIGN KEY (`fk_tipo_familias_id`) REFERENCES `myapp_tipofamilias` (`id`),
  CONSTRAINT `myapp_historiasgeron_fk_tipo_protecciones_4ede1e3b_fk_myapp_tip` FOREIGN KEY (`fk_tipo_protecciones_exequiales_id`) REFERENCES `myapp_tipoproteccionesexequiales` (`id`),
  CONSTRAINT `myapp_historiasgeron_fk_Empleados_id_397f26aa_fk_myapp_usu` FOREIGN KEY (`fk_Empleados_id`) REFERENCES `myapp_usuario` (`id`),
  CONSTRAINT `myapp_historiasgeron_fk_valoraciones_gero_6a2188d9_fk_myapp_val` FOREIGN KEY (`fk_valoraciones_gerontologicas_id`) REFERENCES `myapp_valoracionesgerontologicas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_indicekatz`
--

DROP TABLE IF EXISTS `myapp_indicekatz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_indicekatz` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `alimentacion` tinyint(1) NOT NULL,
  `baño` tinyint(1) NOT NULL,
  `continencia` tinyint(1) NOT NULL,
  `movilidad` tinyint(1) NOT NULL,
  `uso_WC` tinyint(1) NOT NULL,
  `vetido` tinyint(1) NOT NULL,
  `total_puntuacion` smallint NOT NULL,
  `resultado` varchar(255) NOT NULL,
  `observacion_indice_KATZ` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_medicamentos`
--

DROP TABLE IF EXISTS `myapp_medicamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_medicamentos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_medicamento` varchar(255) NOT NULL,
  `dosis` varchar(255) NOT NULL,
  `observacion_medicamento` varchar(255) DEFAULT NULL,
  `alergia` tinyint(1) NOT NULL,
  `nombre_alergia` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_paises`
--

DROP TABLE IF EXISTS `myapp_paises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_paises` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_pais` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_relacionfamilias`
--

DROP TABLE IF EXISTS `myapp_relacionfamilias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_relacionfamilias` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `relacion_mala` longtext NOT NULL,
  `maltrato` tinyint(1) NOT NULL,
  `tipo_maltrato` varchar(255) DEFAULT NULL,
  `tipo_relacion` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_revisionsistemas`
--

DROP TABLE IF EXISTS `myapp_revisionsistemas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_revisionsistemas` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `observaciones_sistemas` longtext NOT NULL,
  `fk_alteraciones_sentidos_id` bigint NOT NULL,
  `fk_sistemas_cardiovasculares_id` bigint NOT NULL,
  `fk_sistemas_digestivos_id` bigint NOT NULL,
  `fk_sistemas_endocrinos_id` bigint NOT NULL,
  `fk_sistemas_intergumentarios_id` bigint NOT NULL,
  `fk_sistemas_nerviosos_id` bigint NOT NULL,
  `fk_sistemas_oseo_musculares_id` bigint NOT NULL,
  `fk_sistemas_respiratorios_id` bigint NOT NULL,
  `fk_sistemas_urinarios_id` bigint NOT NULL,
  `fk_tumores_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fk_alteraciones_sentidos_id` (`fk_alteraciones_sentidos_id`),
  UNIQUE KEY `fk_sistemas_cardiovasculares_id` (`fk_sistemas_cardiovasculares_id`),
  UNIQUE KEY `fk_sistemas_digestivos_id` (`fk_sistemas_digestivos_id`),
  UNIQUE KEY `fk_sistemas_endocrinos_id` (`fk_sistemas_endocrinos_id`),
  UNIQUE KEY `fk_sistemas_intergumentarios_id` (`fk_sistemas_intergumentarios_id`),
  UNIQUE KEY `fk_sistemas_nerviosos_id` (`fk_sistemas_nerviosos_id`),
  UNIQUE KEY `fk_sistemas_oseo_musculares_id` (`fk_sistemas_oseo_musculares_id`),
  UNIQUE KEY `fk_sistemas_respiratorios_id` (`fk_sistemas_respiratorios_id`),
  UNIQUE KEY `fk_sistemas_urinarios_id` (`fk_sistemas_urinarios_id`),
  UNIQUE KEY `fk_tumores_id` (`fk_tumores_id`),
  CONSTRAINT `myapp_revisionsistem_fk_alteraciones_sent_ba674e05_fk_myapp_alt` FOREIGN KEY (`fk_alteraciones_sentidos_id`) REFERENCES `myapp_alteracionsentidos` (`id`),
  CONSTRAINT `myapp_revisionsistem_fk_sistemas_cardiova_5a65831b_fk_myapp_sis` FOREIGN KEY (`fk_sistemas_cardiovasculares_id`) REFERENCES `myapp_sistemascardiovasculares` (`id`),
  CONSTRAINT `myapp_revisionsistem_fk_sistemas_digestiv_4c8d06f5_fk_myapp_sis` FOREIGN KEY (`fk_sistemas_digestivos_id`) REFERENCES `myapp_sistemasdigestivos` (`id`),
  CONSTRAINT `myapp_revisionsistem_fk_sistemas_endocrin_359840ce_fk_myapp_sis` FOREIGN KEY (`fk_sistemas_endocrinos_id`) REFERENCES `myapp_sistemasendocrinos` (`id`),
  CONSTRAINT `myapp_revisionsistem_fk_sistemas_intergum_0093a2e4_fk_myapp_sis` FOREIGN KEY (`fk_sistemas_intergumentarios_id`) REFERENCES `myapp_sistemasintergumentarios` (`id`),
  CONSTRAINT `myapp_revisionsistem_fk_sistemas_nervioso_138aaf14_fk_myapp_sis` FOREIGN KEY (`fk_sistemas_nerviosos_id`) REFERENCES `myapp_sistemasnerviosos` (`id`),
  CONSTRAINT `myapp_revisionsistem_fk_sistemas_oseo_mus_c69c2258_fk_myapp_sis` FOREIGN KEY (`fk_sistemas_oseo_musculares_id`) REFERENCES `myapp_sistemasoseosmusculares` (`id`),
  CONSTRAINT `myapp_revisionsistem_fk_sistemas_respirat_c9f2f10d_fk_myapp_sis` FOREIGN KEY (`fk_sistemas_respiratorios_id`) REFERENCES `myapp_sistemasrespiratorios` (`id`),
  CONSTRAINT `myapp_revisionsistem_fk_sistemas_urinario_52d9ee26_fk_myapp_sis` FOREIGN KEY (`fk_sistemas_urinarios_id`) REFERENCES `myapp_sistemasurinarios` (`id`),
  CONSTRAINT `myapp_revisionsistem_fk_tumores_id_6df50d6a_fk_myapp_tum` FOREIGN KEY (`fk_tumores_id`) REFERENCES `myapp_tumores` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_seguridadessociales`
--

DROP TABLE IF EXISTS `myapp_seguridadessociales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_seguridadessociales` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo_regimen` varchar(1) NOT NULL,
  `nombre_eps` varchar(255) DEFAULT NULL,
  `nombre_ips` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_sindromesproblemas`
--

DROP TABLE IF EXISTS `myapp_sindromesproblemas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_sindromesproblemas` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `vertigo` tinyint(1) NOT NULL,
  `delirio` tinyint(1) NOT NULL,
  `caidas` tinyint(1) NOT NULL,
  `numero_caidas_fractura` smallint NOT NULL,
  `sincope` tinyint(1) NOT NULL,
  `dolor_cronio` tinyint(1) NOT NULL,
  `deprivacion_auditiva` tinyint(1) NOT NULL,
  `deprivacion_visual` tinyint(1) NOT NULL,
  `insomnio` tinyint(1) NOT NULL,
  `incontinencia_urinaria` tinyint(1) NOT NULL,
  `prostatismo` tinyint(1) NOT NULL,
  `estrenhimiento` tinyint(1) NOT NULL,
  `ulcera_presion` tinyint(1) NOT NULL,
  `inmovilizacion` tinyint(1) NOT NULL,
  `cirugia` tinyint(1) NOT NULL,
  `numero_cirugias` smallint NOT NULL,
  `observacion_sindromes_problemas` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_sistemascardiovasculares`
--

DROP TABLE IF EXISTS `myapp_sistemascardiovasculares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_sistemascardiovasculares` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `infarto_miocardio` tinyint(1) NOT NULL,
  `HTA` tinyint(1) NOT NULL,
  `insuficiencia_cardiaca` tinyint(1) NOT NULL,
  `arteriosclerosis` tinyint(1) NOT NULL,
  `otra_alteracion_cardiovascular` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_sistemasdigestivos`
--

DROP TABLE IF EXISTS `myapp_sistemasdigestivos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_sistemasdigestivos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `gastritis` tinyint(1) NOT NULL,
  `diarrea` tinyint(1) NOT NULL,
  `estrenhimiento` tinyint(1) NOT NULL,
  `ulcera_duodenal` tinyint(1) NOT NULL,
  `otra_alteracion_digestiva` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_sistemasendocrinos`
--

DROP TABLE IF EXISTS `myapp_sistemasendocrinos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_sistemasendocrinos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `diabetes_mellitus` tinyint(1) NOT NULL,
  `hipertiroidismo` tinyint(1) NOT NULL,
  `hipotiroidismo` tinyint(1) NOT NULL,
  `bocio` tinyint(1) NOT NULL,
  `incontinencia` tinyint(1) NOT NULL,
  `otra_alteracion_endocrina` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_sistemasintergumentarios`
--

DROP TABLE IF EXISTS `myapp_sistemasintergumentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_sistemasintergumentarios` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `prurito` tinyint(1) NOT NULL,
  `urticaria` tinyint(1) NOT NULL,
  `verruga` tinyint(1) NOT NULL,
  `quemadura` tinyint(1) NOT NULL,
  `otra_alteracion_intergumentaria` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_sistemasnerviosos`
--

DROP TABLE IF EXISTS `myapp_sistemasnerviosos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_sistemasnerviosos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `demencia_senil` tinyint(1) NOT NULL,
  `alzheimer` tinyint(1) NOT NULL,
  `parkinson` tinyint(1) NOT NULL,
  `esquizofrenia` tinyint(1) NOT NULL,
  `eilepsia` tinyint(1) NOT NULL,
  `otra_alteracion_nerviosa` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_sistemasoseosmusculares`
--

DROP TABLE IF EXISTS `myapp_sistemasoseosmusculares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_sistemasoseosmusculares` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `artritis` tinyint(1) NOT NULL,
  `osteoporosis` tinyint(1) NOT NULL,
  `osteartritis` tinyint(1) NOT NULL,
  `lumbago` tinyint(1) NOT NULL,
  `otra_alteracion_osea` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_sistemasrespiratorios`
--

DROP TABLE IF EXISTS `myapp_sistemasrespiratorios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_sistemasrespiratorios` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `epoc` tinyint(1) NOT NULL,
  `bronquitis` tinyint(1) NOT NULL,
  `asma` tinyint(1) NOT NULL,
  `neumonia` tinyint(1) NOT NULL,
  `otra_alteracion_respiratoria` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_sistemasurinarios`
--

DROP TABLE IF EXISTS `myapp_sistemasurinarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_sistemasurinarios` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `anuria` tinyint(1) NOT NULL,
  `cistitis` tinyint(1) NOT NULL,
  `prostatitis` tinyint(1) NOT NULL,
  `prolapso_genital` tinyint(1) NOT NULL,
  `incontinencia` tinyint(1) NOT NULL,
  `otra_alteracion_urinaria` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_situacionesgerontologicas`
--

DROP TABLE IF EXISTS `myapp_situacionesgerontologicas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_situacionesgerontologicas` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fk_evaluaciones_bucales_id` bigint NOT NULL,
  `fk_sindromes_problemas_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fk_evaluaciones_bucales_id` (`fk_evaluaciones_bucales_id`),
  UNIQUE KEY `fk_sindromes_problemas_id` (`fk_sindromes_problemas_id`),
  CONSTRAINT `myapp_situacionesger_fk_evaluaciones_buca_3edeed4f_fk_myapp_eva` FOREIGN KEY (`fk_evaluaciones_bucales_id`) REFERENCES `myapp_evaluaciones_bucales` (`id`),
  CONSTRAINT `myapp_situacionesger_fk_sindromes_problem_86c5285b_fk_myapp_sin` FOREIGN KEY (`fk_sindromes_problemas_id`) REFERENCES `myapp_sindromesproblemas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_tipodocumentos`
--

DROP TABLE IF EXISTS `myapp_tipodocumentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_tipodocumentos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo_documento` varchar(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_tipofamilias`
--

DROP TABLE IF EXISTS `myapp_tipofamilias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_tipofamilias` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `familia_nuclear` tinyint(1) NOT NULL,
  `familia_extensa` tinyint(1) NOT NULL,
  `familia_ampliada` tinyint(1) NOT NULL,
  `familia_multiespecial` tinyint(1) NOT NULL,
  `familia_compuesta` tinyint(1) NOT NULL,
  `familia_monoparental_simple` tinyint(1) NOT NULL,
  `familia_monoparental_compuesta` tinyint(1) NOT NULL,
  `familia_homoparental` tinyint(1) NOT NULL,
  `familia_unipersonal` tinyint(1) NOT NULL,
  `familia_pareja_sin_hijos` tinyint(1) NOT NULL,
  `familia_mixta` tinyint(1) NOT NULL,
  `unidad_domestica` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_tipoproteccionesexequiales`
--

DROP TABLE IF EXISTS `myapp_tipoproteccionesexequiales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_tipoproteccionesexequiales` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `proteccion` tinyint(1) NOT NULL,
  `nombre_entidad` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_tumores`
--

DROP TABLE IF EXISTS `myapp_tumores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_tumores` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tejido_mamario` tinyint(1) NOT NULL,
  `sistema_digestivo` tinyint(1) NOT NULL,
  `sistema_urinario` tinyint(1) NOT NULL,
  `otra_tumor` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_usuario`
--

DROP TABLE IF EXISTS `myapp_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_usuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `segundo_apellido` varchar(100) NOT NULL,
  `celular` varchar(30) NOT NULL,
  `tel_fijo` varchar(30) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `grupo_sanguineo` varchar(3) NOT NULL,
  `genero` varchar(50) NOT NULL,
  `matricula_profesional` varchar(255) NOT NULL,
  `numero_documento` varchar(50) NOT NULL,
  `sexo` varchar(1) NOT NULL,
  `estado_civil` varchar(11) NOT NULL,
  `lugar_tipo_procedencia` varchar(1) NOT NULL,
  `fk_ciudad_id` bigint NOT NULL,
  `fk_datos_socioeconomicos_id` bigint NOT NULL,
  `fk_espiritualidades_id` bigint NOT NULL,
  `fk_habitos_id` bigint NOT NULL,
  `fk_seguridades_sociales_id` bigint NOT NULL,
  `fk_tipo_documento_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fk_datos_socioeconomicos_id` (`fk_datos_socioeconomicos_id`),
  UNIQUE KEY `fk_espiritualidades_id` (`fk_espiritualidades_id`),
  UNIQUE KEY `fk_habitos_id` (`fk_habitos_id`),
  UNIQUE KEY `fk_seguridades_sociales_id` (`fk_seguridades_sociales_id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `myapp_usuario_fk_ciudad_id_66c7d485_fk_myapp_ciudades_id` (`fk_ciudad_id`),
  KEY `myapp_usuario_fk_tipo_documento_id_db36d533_fk_myapp_tip` (`fk_tipo_documento_id`),
  CONSTRAINT `myapp_usuario_fk_ciudad_id_66c7d485_fk_myapp_ciudades_id` FOREIGN KEY (`fk_ciudad_id`) REFERENCES `myapp_ciudades` (`id`),
  CONSTRAINT `myapp_usuario_fk_datos_socioeconom_adcd9db0_fk_myapp_dat` FOREIGN KEY (`fk_datos_socioeconomicos_id`) REFERENCES `myapp_datossocioeconomicos` (`id`),
  CONSTRAINT `myapp_usuario_fk_espiritualidades__2a59cada_fk_myapp_esp` FOREIGN KEY (`fk_espiritualidades_id`) REFERENCES `myapp_espiritualidades` (`id`),
  CONSTRAINT `myapp_usuario_fk_habitos_id_93529585_fk_myapp_habitos_id` FOREIGN KEY (`fk_habitos_id`) REFERENCES `myapp_habitos` (`id`),
  CONSTRAINT `myapp_usuario_fk_seguridades_socia_2f38299d_fk_myapp_seg` FOREIGN KEY (`fk_seguridades_sociales_id`) REFERENCES `myapp_seguridadessociales` (`id`),
  CONSTRAINT `myapp_usuario_fk_tipo_documento_id_db36d533_fk_myapp_tip` FOREIGN KEY (`fk_tipo_documento_id`) REFERENCES `myapp_tipodocumentos` (`id`),
  CONSTRAINT `myapp_usuario_user_id_ef9ad113_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_valoracionesgerontologicas`
--

DROP TABLE IF EXISTS `myapp_valoracionesgerontologicas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_valoracionesgerontologicas` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `aspecto_sociales` varchar(100) NOT NULL,
  `aspecto_fisicos` varchar(100) NOT NULL,
  `aspectos_funcional` varchar(100) NOT NULL,
  `aspectos_psicogerontologico` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_valoracionesmentales`
--

DROP TABLE IF EXISTS `myapp_valoracionesmentales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_valoracionesmentales` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_actual_pregunta` tinyint(1) NOT NULL,
  `dia_semana_pregunta` tinyint(1) NOT NULL,
  `lugar_pregunta` tinyint(1) NOT NULL,
  `lugar_nacimiento_pregunta` tinyint(1) NOT NULL,
  `presidente_pregunta` tinyint(1) NOT NULL,
  `primer_apellido_madre_pregunta` tinyint(1) NOT NULL,
  `resta_pregunta` tinyint(1) NOT NULL,
  `total_puntuacion_valoracion_mental` smallint NOT NULL,
  `resultado` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-14 17:36:42
