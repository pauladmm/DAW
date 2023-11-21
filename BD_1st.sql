-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 15-11-2023 a las 20:19:08
-- Versión del servidor: 10.3.27-MariaDB-0+deb10u1
-- Versión de PHP: 7.4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `fútbol`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipo`
--

CREATE TABLE `equipo` (
  `cod_equipo` int(5) NOT NULL,
  `nombre` text NOT NULL,
  `estadio` text NOT NULL,
  `aforo` int(3) NOT NULL,
  `año fundacion` year(4) NOT NULL,
  `ciudad` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `goles`
--

CREATE TABLE `goles` (
  `cod_jugador` int(5) NOT NULL,
  `cod_partido` int(5) NOT NULL,
  `minuto` int(2) NOT NULL,
  `descripcion` text NOT NULL,
  `numero` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jugadores`
--

CREATE TABLE `jugadores` (
  `cod_jugador` int(5) NOT NULL,
  `nombre` text NOT NULL,
  `fecha nacimiento` date NOT NULL,
  `posición` text NOT NULL,
  `cod_equipo` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partido`
--

CREATE TABLE `partido` (
  `cod_partido` int(5) NOT NULL,
  `fecha partido` date NOT NULL,
  `goles fuera` int(2) NOT NULL,
  `goles casa` int(2) NOT NULL,
  `cod_equipo_fuera` int(5) NOT NULL,
  `cod_equipo_casa` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presidente`
--

CREATE TABLE `presidente` (
  `dni` int(9) NOT NULL,
  `fecha nacimiento` date NOT NULL,
  `año de eleccion` year(4) NOT NULL,
  `equipo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `equipo`
--
ALTER TABLE `equipo`
  ADD PRIMARY KEY (`cod_equipo`);

--
-- Indices de la tabla `goles`
--
ALTER TABLE `goles`
  ADD KEY `cod_jugador` (`cod_jugador`),
  ADD KEY `cod_partido` (`cod_partido`);

--
-- Indices de la tabla `jugadores`
--
ALTER TABLE `jugadores`
  ADD PRIMARY KEY (`cod_jugador`),
  ADD KEY `cod_equipo` (`cod_equipo`);

--
-- Indices de la tabla `partido`
--
ALTER TABLE `partido`
  ADD PRIMARY KEY (`cod_partido`),
  ADD KEY `cod_equipo_casa` (`cod_equipo_casa`),
  ADD KEY `cod_equipo_fuera` (`cod_equipo_fuera`);

--
-- Indices de la tabla `presidente`
--
ALTER TABLE `presidente`
  ADD PRIMARY KEY (`dni`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `goles`
--
ALTER TABLE `goles`
  ADD CONSTRAINT `cod_jugador` FOREIGN KEY (`cod_jugador`) REFERENCES `jugadores` (`cod_jugador`),
  ADD CONSTRAINT `cod_partido` FOREIGN KEY (`cod_partido`) REFERENCES `partido` (`cod_partido`);

--
-- Filtros para la tabla `jugadores`
--
ALTER TABLE `jugadores`
  ADD CONSTRAINT `cod_equipo` FOREIGN KEY (`cod_equipo`) REFERENCES `equipo` (`cod_equipo`);

--
-- Filtros para la tabla `partido`
--
ALTER TABLE `partido`
  ADD CONSTRAINT `cod_equipo_casa` FOREIGN KEY (`cod_equipo_casa`) REFERENCES `equipo` (`cod_equipo`),
  ADD CONSTRAINT `cod_equipo_fuera` FOREIGN KEY (`cod_equipo_fuera`) REFERENCES `equipo` (`cod_equipo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

--
-- Algunos comandos para crear usuario y modificar sus privilegios
--

CREATE USER 'myuser'@'%' 
IDENTIFIED VIA mysql_native_password USING '***';
GRANT USAGE ON *.* TO 'myuser'@'%' 
REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

CREATE USER 'testUser'@'%' 
IDENTIFIED VIA mysql_native_password USING '***';
GRANT SELECT, UPDATE ON *.* TO 'testUser'@'%' 
REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

CREATE USER 'customer1'@'%' 
IDENTIFIED VIA mysql_native_password USING '***';
GRANT USAGE ON *.* TO 'customer1'@'%' 
REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

DROP USER myuser;

CREATE USER 'grantUser'@'%' IDENTIFIED VIA mysql_native_password USING '***';
GRANT SELECT, INSERT ON *.* TO 'grantUser'@'%' 
REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

REVOKE ALL PRIVILEGES ON *.* FROM 'grantUser'@'%'

REVOKE ALL PRIVILEGES ON *.* FROM 'testUser'@'%'; 
REVOKE GRANT OPTION ON *.* FROM 'testUser'@'%'; 
GRANT SELECT ON *.* TO 'testUser'@'%'
