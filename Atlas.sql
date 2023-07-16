SET SERVEROUTPUT ON;

/*
    
    SCRIPT BASE DE DATOS CLINIC CARE
    LENGUAJE DE BASE DE DATOS
    GRUPO ATLAS
    
    INTEGRANTES:
    Athuro Chaves Aguilar
    Catalina Chaves Aguilar 
    David Rodriguez Castillo
    Mathias Jimenes Prendas
    
*/

--Creacion de Tablas

CREATE TABLE PACIENTES (
    ID_PACIENTE NUMBER PRIMARY KEY,
    NOMBRE VARCHAR2(50),
    APELLIDO VARCHAR2(50),
    FECHA_NACIMIENTO DATE,
    GENERO CHAR(1),
    DIRECCION VARCHAR2(200),
    TELEFONO VARCHAR2(15),
    CORREO_ELECTRONICO VARCHAR2(100)
);


CREATE TABLE EMPLEADOS (
    ID_EMPLEADO NUMBER PRIMARY KEY,
    NOMBRE_EMPLEADO VARCHAR2(50),
    APELLIDO_EMPLEADO VARCHAR2(50),
    CARGO VARCHAR2(50),
    FECHA_CONTRATACION DATE,
    SALARIO NUMBER(10,2)
);

CREATE TABLE PROVEEDORES (
    ID_PROVEEDOR NUMBER PRIMARY KEY,
    NOMBRE_PROVEEDOR VARCHAR2 (50),
    DIRECCION VARCHAR2(100),
    CORREO_PROVEEDOR VARCHAR2(100)
);

CREATE TABLE PRODUCTOS (
    ID_PRODUCTO NUMBER PRIMARY KEY,
    ID_PROVEEDOR NUMBER,
    CANTIDAD NUMBER,
    DESCRIPCION VARCHAR2(100),
    PRECIO_PRODUCTO NUMBER(10,2),
    FOREIGN KEY (ID_PROVEEDOR) REFERENCES PROVEEDORES(ID_PROVEEDOR)
);

CREATE TABLE TRATAMIENTOS (
    ID_TRATAMIENTO NUMBER PRIMARY KEY,
    ID_PRODUCTO NUMBER,
    DESCRIPCION VARCHAR2(100),
    DURACION_ESTIMADA NUMBER,
    PRECIO_TRATAMIENTO NUMBER(10,2),
    FOREIGN KEY (ID_PRODUCTO) REFERENCES PRODUCTOS(ID_PRODUCTO)
);

CREATE TABLE CITAS (
    ID_CITA NUMBER PRIMARY KEY,
    ID_PACIENTE NUMBER,
    ID_EMPLEADO NUMBER,
    ID_TRATAMIENTO NUMBER,
    FECHA_CITA DATE,
    HORA_CITA TIMESTAMP,
    OBSERVACIONES VARCHAR2(200),
    FOREIGN KEY (ID_PACIENTE) REFERENCES PACIENTES(ID_PACIENTE),
    FOREIGN KEY (ID_EMPLEADO) REFERENCES EMPLEADOS(ID_EMPLEADO),
    FOREIGN KEY (ID_TRATAMIENTO) REFERENCES TRATAMIENTOS(ID_TRATAMIENTO)
);

CREATE TABLE FACTURAS (
    ID_FACTURA NUMBER PRIMARY KEY,
    ID_CITA NUMBER,
    FECHA_EMISION DATE,
    SUBTOTAL NUMBER(10, 2),
    IMPUESTOS NUMBER(10, 2),
    TOTAL NUMBER(10, 2),
    FOREIGN KEY (ID_CITA) REFERENCES CITA(ID_CITA)
);

--Insercion a Tablas



--Creacion de Usuarios

CREATE USER ADMINISTRADOR IDENTIFIED BY administrador123;
GRANT DBA TO ADMINISTRADOR;

CREATE USER RECEPCIONISTA IDENTIFIED BY recepcionista123;
GRANT CREATE SESSION, CREATE TABLE, INSERT ANY TABLE, UPDATE ANY TABLE TO RECEPCIONISTA;

--Restricciones de Tablas Y 2 Usuarios 



--25 Procedimientos Almacenados



--10 Vistas



--15 Funciones



--10 Paquetes



--5 Triggers



--15 Cursores



