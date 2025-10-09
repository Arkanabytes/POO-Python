SQL
-- Crear la base de datos (opcional, si no existe)
CREATE DATABASE IF NOT EXISTS empresa;
USE empresa;

-- Tabla para los tipos de cliente
CREATE TABLE TIPO (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(45) NOT NULL,
    PRIMARY KEY (id)
);

-- Tabla para los clientes
CREATE TABLE CLIENTE (
    id INT NOT NULL AUTO_INCREMENT,
    run VARCHAR(13) NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    direccion VARCHAR(45),
    fono INT,
    correo VARCHAR(45),
    montoCredito INT,
    deuda INT,
    TIPO_id INT NOT NULL,
    PRIMARY KEY (id),
    INDEX fk_CLIENTE_TIPO_idx (TIPO_id ASC),
    CONSTRAINT fk_CLIENTE_TIPO
        FOREIGN KEY (TIPO_id)
        REFERENCES TIPO (id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

-- Tabla para los usuarios del sistema
CREATE TABLE usuarios (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password_hash VARCHAR(120) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    tipo_usuario ENUM('Administrador', 'Vendedor') NOT NULL,
    fecha_registro TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE INDEX username_UNIQUE (username ASC)
);

-- Opcional: Insertar datos iniciales para la tabla TIPO
INSERT INTO TIPO (nombre) VALUES ('Cliente Nuevo'), ('Cliente Regular'), ('Cliente VIP');