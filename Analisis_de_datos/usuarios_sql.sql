CREATE DATABASE prueba_sql;
USE prueba_sql;

CREATE TABLE usuarios(
	idUsuario INT NOT NULL AUTO_INCREMENT,
    nombreUsuario VARCHAR(20) NOT NULL,
    apellidoUsuario VARCHAR(25) NOT NULL,
    cedulaUsuario VARCHAR(10) NOT NULL,
    PRIMARY KEY (idUsuario)
);

