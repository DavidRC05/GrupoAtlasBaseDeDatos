SET SERVEROUTPUT ON;

/*
    
    SCRIPT BASEA DE DATOS CLINIC CARE
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
    FOREIGN KEY (ID_CITA) REFERENCES CITAS(ID_CITA)
);

--Insercion a Tablas



INSERT INTO PACIENTES (ID_PACIENTE, NOMBRE, APELLIDO, FECHA_NACIMIENTO, GENERO, DIRECCION, TELEFONO, CORREO_ELECTRONICO)
VALUES (1, 'Juan', 'Perez', TO_DATE('1990-01-15','YYYY-MM-DD'), 'M', 'Calle Falsa 123, Ciudad X', '1234567890', 'juan.perez@mail.com');

INSERT INTO PACIENTES (ID_PACIENTE, NOMBRE, APELLIDO, FECHA_NACIMIENTO, GENERO, DIRECCION, TELEFONO, CORREO_ELECTRONICO)
VALUES (2, 'Ana', 'Gomez', TO_DATE('1985-05-25','YYYY-MM-DD'), 'F', 'Avenida Real 456, Ciudad Y', '0987654321', 'ana.gomez@mail.com');

INSERT INTO PACIENTES (ID_PACIENTE, NOMBRE, APELLIDO, FECHA_NACIMIENTO, GENERO, DIRECCION, TELEFONO, CORREO_ELECTRONICO)
VALUES (3, 'Carlos', 'Lopez', TO_DATE('1975-10-05','YYYY-MM-DD'), 'M', 'Bulevar Sol 789, Ciudad Z', '1112223334', 'carlos.lopez@mail.com');

INSERT INTO PACIENTES (ID_PACIENTE, NOMBRE, APELLIDO, FECHA_NACIMIENTO, GENERO, DIRECCION, TELEFONO, CORREO_ELECTRONICO)
VALUES (4, 'Maria', 'Sanchez', TO_DATE('1999-04-30','YYYY-MM-DD'), 'F', 'Callejon Oscuro 321, Ciudad A', '5554443332', 'maria.sanchez@mail.com');

INSERT INTO PACIENTES (ID_PACIENTE, NOMBRE, APELLIDO, FECHA_NACIMIENTO, GENERO, DIRECCION, TELEFONO, CORREO_ELECTRONICO)
VALUES (5, 'Jose', 'Martinez', TO_DATE('1980-07-20','YYYY-MM-DD'), 'M', 'Paseo Luna 654, Ciudad B', '6667778889', 'jose.martinez@mail.com');



INSERT INTO EMPLEADOS (ID_EMPLEADO, NOMBRE_EMPLEADO, APELLIDO_EMPLEADO, CARGO, FECHA_CONTRATACION, SALARIO)
VALUES (1, 'Luis', 'Gonzalez', 'Recepcionista', TO_DATE('2010-05-01','YYYY-MM-DD'), 7000.00);

INSERT INTO EMPLEADOS (ID_EMPLEADO, NOMBRE_EMPLEADO, APELLIDO_EMPLEADO, CARGO, FECHA_CONTRATACION, SALARIO)
VALUES (2, 'Laura', 'Fernandez', 'Enfermera', TO_DATE('2015-08-15','YYYY-MM-DD'), 5000.00);

INSERT INTO EMPLEADOS (ID_EMPLEADO, NOMBRE_EMPLEADO, APELLIDO_EMPLEADO, CARGO, FECHA_CONTRATACION, SALARIO)
VALUES (3, 'Andrea', 'Ramirez', 'Doctora', TO_DATE('2005-10-10','YYYY-MM-DD'), 7500.00);

INSERT INTO EMPLEADOS (ID_EMPLEADO, NOMBRE_EMPLEADO, APELLIDO_EMPLEADO, CARGO, FECHA_CONTRATACION, SALARIO)
VALUES (4, 'Isabel', 'Morales', 'Enfermera', TO_DATE('2012-03-20','YYYY-MM-DD'), 5500.00);

INSERT INTO EMPLEADOS (ID_EMPLEADO, NOMBRE_EMPLEADO, APELLIDO_EMPLEADO, CARGO, FECHA_CONTRATACION, SALARIO)
VALUES (5, 'David', 'Castillo', 'Doctor', TO_DATE('2018-06-01','YYYY-MM-DD'), 7200.00);



INSERT INTO PROVEEDORES (ID_PROVEEDOR, NOMBRE_PROVEEDOR, DIRECCION, CORREO_PROVEEDOR)
VALUES (1, 'Proveedora XYZ', 'Calle Industria 123, Ciudad X', 'contacto@proveedoraXYZ.com');

INSERT INTO PROVEEDORES (ID_PROVEEDOR, NOMBRE_PROVEEDOR, DIRECCION, CORREO_PROVEEDOR)
VALUES (2, 'Suplidora ABC', 'Avenida Comercio 456, Ciudad Y', 'info@suplidoraABC.com');

INSERT INTO PROVEEDORES (ID_PROVEEDOR, NOMBRE_PROVEEDOR, DIRECCION, CORREO_PROVEEDOR)
VALUES (3, 'Distribuidora LMN', 'Bulevar Negocios 789, Ciudad Z', 'atencion@distribuidoraLMN.com');

INSERT INTO PROVEEDORES (ID_PROVEEDOR, NOMBRE_PROVEEDOR, DIRECCION, CORREO_PROVEEDOR)
VALUES (4, 'Abastecedora RST', 'Callejon Servicios 321, Ciudad A', 'clientes@abastecedoraRST.com');

INSERT INTO PROVEEDORES (ID_PROVEEDOR, NOMBRE_PROVEEDOR, DIRECCION, CORREO_PROVEEDOR)
VALUES (5, 'Proveedor JKL', 'Paseo Ventas 654, Ciudad B', 'soporte@proveedorJKL.com');



INSERT INTO PRODUCTOS (ID_PRODUCTO, ID_PROVEEDOR, CANTIDAD, DESCRIPCION, PRECIO_PRODUCTO)
VALUES (1, 1, 50, 'Medicamento A', 20.00);

INSERT INTO PRODUCTOS (ID_PRODUCTO, ID_PROVEEDOR, CANTIDAD, DESCRIPCION, PRECIO_PRODUCTO)
VALUES (2, 2, 100, 'Medicamento B', 15.50);

INSERT INTO PRODUCTOS (ID_PRODUCTO, ID_PROVEEDOR, CANTIDAD, DESCRIPCION, PRECIO_PRODUCTO)
VALUES (3, 3, 200, 'Medicamento C', 25.30);

INSERT INTO PRODUCTOS (ID_PRODUCTO, ID_PROVEEDOR, CANTIDAD, DESCRIPCION, PRECIO_PRODUCTO)
VALUES (4, 4, 150, 'Medicamento D', 22.10);

INSERT INTO PRODUCTOS (ID_PRODUCTO, ID_PROVEEDOR, CANTIDAD, DESCRIPCION, PRECIO_PRODUCTO)
VALUES (5, 5, 175, 'Medicamento E', 18.75);



INSERT INTO TRATAMIENTOS (ID_TRATAMIENTO, ID_PRODUCTO, DESCRIPCION, DURACION_ESTIMADA, PRECIO_TRATAMIENTO)
VALUES (1, 1, 'Tratamiento para la condici�n X', 30, 120.00);

INSERT INTO TRATAMIENTOS (ID_TRATAMIENTO, ID_PRODUCTO, DESCRIPCION, DURACION_ESTIMADA, PRECIO_TRATAMIENTO)
VALUES (2, 2, 'Tratamiento para la condici�n Y', 45, 200.00);

INSERT INTO TRATAMIENTOS (ID_TRATAMIENTO, ID_PRODUCTO, DESCRIPCION, DURACION_ESTIMADA, PRECIO_TRATAMIENTO)
VALUES (3, 3, 'Tratamiento para la condici�n Z', 60, 300.00);

INSERT INTO TRATAMIENTOS (ID_TRATAMIENTO, ID_PRODUCTO, DESCRIPCION, DURACION_ESTIMADA, PRECIO_TRATAMIENTO)
VALUES (4, 4, 'Tratamiento para la condici�n A', 20, 100.00);

INSERT INTO TRATAMIENTOS (ID_TRATAMIENTO, ID_PRODUCTO, DESCRIPCION, DURACION_ESTIMADA, PRECIO_TRATAMIENTO)
VALUES (5, 5, 'Tratamiento para la condici�n B', 40, 150.00);



INSERT INTO CITAS (ID_CITA, ID_PACIENTE, ID_EMPLEADO, ID_TRATAMIENTO, FECHA_CITA, HORA_CITA, OBSERVACIONES)
VALUES (1, 1, 1, 1, TO_DATE('2023-07-20', 'YYYY-MM-DD'), TO_TIMESTAMP('08:00:00', 'HH24:MI:SS'), 'Primera cita');

INSERT INTO CITAS (ID_CITA, ID_PACIENTE, ID_EMPLEADO, ID_TRATAMIENTO, FECHA_CITA, HORA_CITA, OBSERVACIONES)
VALUES (2, 2, 2, 2, TO_DATE('2023-07-21', 'YYYY-MM-DD'), TO_TIMESTAMP('09:00:00', 'HH24:MI:SS'), 'Cita de seguimiento');

INSERT INTO CITAS (ID_CITA, ID_PACIENTE, ID_EMPLEADO, ID_TRATAMIENTO, FECHA_CITA, HORA_CITA, OBSERVACIONES)
VALUES (3, 3, 3, 3, TO_DATE('2023-07-22', 'YYYY-MM-DD'), TO_TIMESTAMP('10:00:00', 'HH24:MI:SS'), 'Consulta general');

INSERT INTO CITAS (ID_CITA, ID_PACIENTE, ID_EMPLEADO, ID_TRATAMIENTO, FECHA_CITA, HORA_CITA, OBSERVACIONES)
VALUES (4, 4, 4, 4, TO_DATE('2023-07-23', 'YYYY-MM-DD'), TO_TIMESTAMP('11:00:00', 'HH24:MI:SS'), 'Revisi�n de tratamiento');

INSERT INTO CITAS (ID_CITA, ID_PACIENTE, ID_EMPLEADO, ID_TRATAMIENTO, FECHA_CITA, HORA_CITA, OBSERVACIONES)
VALUES (5, 5, 5, 5, TO_DATE('2023-07-24', 'YYYY-MM-DD'), TO_TIMESTAMP('12:00:00', 'HH24:MI:SS'), 'Cita de emergencia');



INSERT INTO FACTURAS (ID_FACTURA, ID_CITA, FECHA_EMISION, SUBTOTAL, IMPUESTOS, TOTAL)
VALUES (1, 1, TO_DATE('2023-07-20', 'YYYY-MM-DD'), 100.00, 20.00, 120.00);

INSERT INTO FACTURAS (ID_FACTURA, ID_CITA, FECHA_EMISION, SUBTOTAL, IMPUESTOS, TOTAL)
VALUES (2, 2, TO_DATE('2023-07-21', 'YYYY-MM-DD'), 150.00, 30.00, 180.00);

INSERT INTO FACTURAS (ID_FACTURA, ID_CITA, FECHA_EMISION, SUBTOTAL, IMPUESTOS, TOTAL)
VALUES (3, 3, TO_DATE('2023-07-22', 'YYYY-MM-DD'), 200.00, 40.00, 240.00);

INSERT INTO FACTURAS (ID_FACTURA, ID_CITA, FECHA_EMISION, SUBTOTAL, IMPUESTOS, TOTAL)
VALUES (4, 4, TO_DATE('2023-07-23', 'YYYY-MM-DD'), 250.00, 50.00, 300.00);

INSERT INTO FACTURAS (ID_FACTURA, ID_CITA, FECHA_EMISION, SUBTOTAL, IMPUESTOS, TOTAL)
VALUES (5, 5, TO_DATE('2023-07-24', 'YYYY-MM-DD'), 300.00, 60.00, 360.00);



--Creacion de Usuarios

CREATE USER C##ADMINISTRADOR IDENTIFIED BY administrador123;
GRANT DBA TO ADMINISTRADOR;

CREATE USER C##RECEPCIONISTA IDENTIFIED BY recepcionista123;
GRANT CREATE SESSION, CREATE TABLE, INSERT ANY TABLE, UPDATE ANY TABLE TO RECEPCIONISTA;

--Restricciones de Tablas Y Usuarios 



--25 Procedimientos Almacenados



CREATE OR REPLACE PROCEDURE SP_INSERT_PACIENTE(
    p_id_paciente IN PACIENTES.ID_PACIENTE%TYPE,
    p_nombre IN PACIENTES.NOMBRE%TYPE,
    p_apellido IN PACIENTES.APELLIDO%TYPE,
    p_fecha_nacimiento IN PACIENTES.FECHA_NACIMIENTO%TYPE,
    p_genero IN PACIENTES.GENERO%TYPE,
    p_direccion IN PACIENTES.DIRECCION%TYPE,
    p_telefono IN PACIENTES.TELEFONO%TYPE,
    p_correo_electronico IN PACIENTES.CORREO_ELECTRONICO%TYPE)
IS
BEGIN
    INSERT INTO PACIENTES(ID_PACIENTE, NOMBRE, APELLIDO, FECHA_NACIMIENTO, GENERO, DIRECCION, TELEFONO, CORREO_ELECTRONICO)
    VALUES (p_id_paciente, p_nombre, p_apellido, p_fecha_nacimiento, p_genero, p_direccion, p_telefono, p_correo_electronico);
    DBMS_OUTPUT.PUT_LINE('DATOS INSERTADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el paciente con el ID: ' || p_id_paciente);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_INSERT_PACIENTE;



CREATE OR REPLACE PROCEDURE SP_SELECT_PACIENTE(p_id_paciente IN PACIENTES.ID_PACIENTE%TYPE)
IS
    v_nombre PACIENTES.NOMBRE%TYPE;
    v_apellido PACIENTES.APELLIDO%TYPE;
    v_fecha_nacimiento PACIENTES.FECHA_NACIMIENTO%TYPE;
    v_genero PACIENTES.GENERO%TYPE;
    v_direccion PACIENTES.DIRECCION%TYPE;
    v_telefono PACIENTES.TELEFONO%TYPE;
    v_correo_electronico PACIENTES.CORREO_ELECTRONICO%TYPE;
BEGIN
    SELECT NOMBRE, APELLIDO, FECHA_NACIMIENTO, GENERO, DIRECCION, TELEFONO, CORREO_ELECTRONICO
    INTO v_nombre, v_apellido, v_fecha_nacimiento, v_genero, v_direccion, v_telefono, v_correo_electronico
    FROM PACIENTES
    WHERE ID_PACIENTE = p_id_paciente;

    DBMS_OUTPUT.PUT_LINE('Nombre: ' || v_nombre || ', Apellido: ' || v_apellido || ', Fecha de Nacimiento: ' || TO_CHAR(v_fecha_nacimiento, 'DD-MON-YYYY') 
                         || ', G�nero: ' || v_genero || ', Direcci�n: ' || v_direccion || ', Tel�fono: ' || v_telefono || ', Correo electr�nico: ' || v_correo_electronico);
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el paciente con el ID: ' || p_id_paciente);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_SELECT_PACIENTE;



CREATE OR REPLACE PROCEDURE SP_UPDATE_PACIENTE(
    p_id_paciente IN PACIENTES.ID_PACIENTE%TYPE,
    p_nombre IN PACIENTES.NOMBRE%TYPE,
    p_apellido IN PACIENTES.APELLIDO%TYPE,
    p_fecha_nacimiento IN PACIENTES.FECHA_NACIMIENTO%TYPE,
    p_genero IN PACIENTES.GENERO%TYPE,
    p_direccion IN PACIENTES.DIRECCION%TYPE,
    p_telefono IN PACIENTES.TELEFONO%TYPE,
    p_correo_electronico IN PACIENTES.CORREO_ELECTRONICO%TYPE)
IS
BEGIN
    UPDATE PACIENTES
    SET 
        NOMBRE = p_nombre,
        APELLIDO = p_apellido,
        FECHA_NACIMIENTO = p_fecha_nacimiento,
        GENERO = p_genero,
        DIRECCION = p_direccion,
        TELEFONO = p_telefono,
        CORREO_ELECTRONICO = p_correo_electronico
    WHERE ID_PACIENTE = p_id_paciente;
    DBMS_OUTPUT.PUT_LINE('DATOS ACTUALIZADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el paciente con el ID: ' || p_id_paciente);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_UPDATE_PACIENTE;



CREATE OR REPLACE PROCEDURE SP_DELETE_PACIENTE(p_id_paciente IN PACIENTES.ID_PACIENTE%TYPE)
IS
BEGIN
    DELETE FROM PACIENTES
    WHERE ID_PACIENTE = p_id_paciente;
DBMS_OUTPUT.PUT_LINE('DATOS ELIMINADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el paciente con el ID: ' || p_id_paciente);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_DELETE_PACIENTE;











CREATE OR REPLACE PROCEDURE SP_INSERT_EMPLEADO(
    p_id_empleado IN EMPLEADOS.ID_EMPLEADO%TYPE,
    p_nombre_empleado IN EMPLEADOS.NOMBRE_EMPLEADO%TYPE,
    p_apellido_empleado IN EMPLEADOS.APELLIDO_EMPLEADO%TYPE,
    p_cargo IN EMPLEADOS.CARGO%TYPE,
    p_fecha_contratacion IN EMPLEADOS.FECHA_CONTRATACION%TYPE,
    p_salario IN EMPLEADOS.SALARIO%TYPE)
IS
BEGIN
    INSERT INTO EMPLEADOS(ID_EMPLEADO, NOMBRE_EMPLEADO, APELLIDO_EMPLEADO, CARGO, FECHA_CONTRATACION, SALARIO)
    VALUES (p_id_empleado, p_nombre_empleado, p_apellido_empleado, p_cargo, p_fecha_contratacion, p_salario);
    DBMS_OUTPUT.PUT_LINE('DATOS INSERTADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el empleado con el ID: ' || p_id_empleado);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_INSERT_EMPLEADO;



CREATE OR REPLACE PROCEDURE SP_SELECT_EMPLEADO(p_id_empleado IN EMPLEADOS.ID_EMPLEADO%TYPE)
IS
    v_nombre_empleado EMPLEADOS.NOMBRE_EMPLEADO%TYPE;
    v_apellido_empleado EMPLEADOS.APELLIDO_EMPLEADO%TYPE;
    v_cargo EMPLEADOS.CARGO%TYPE;
    v_fecha_contratacion EMPLEADOS.FECHA_CONTRATACION%TYPE;
    v_salario EMPLEADOS.SALARIO%TYPE;
BEGIN
    SELECT NOMBRE_EMPLEADO, APELLIDO_EMPLEADO, CARGO, FECHA_CONTRATACION, SALARIO
    INTO v_nombre_empleado, v_apellido_empleado, v_cargo, v_fecha_contratacion, v_salario
    FROM EMPLEADOS
    WHERE ID_EMPLEADO = p_id_empleado;

    DBMS_OUTPUT.PUT_LINE('Nombre Empleado: ' || v_nombre_empleado || ', Apellido Empleado: ' || v_apellido_empleado || ', Cargo: ' || v_cargo || ', Fecha Contrataci�n: ' || TO_CHAR(v_fecha_contratacion, 'DD-MON-YYYY') 
                         || ', Salario: ' || v_salario);
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el empleado con el ID: ' || p_id_empleado);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_SELECT_EMPLEADO;



CREATE OR REPLACE PROCEDURE SP_UPDATE_EMPLEADO(
    p_id_empleado IN EMPLEADOS.ID_EMPLEADO%TYPE,
    p_nombre_empleado IN EMPLEADOS.NOMBRE_EMPLEADO%TYPE,
    p_apellido_empleado IN EMPLEADOS.APELLIDO_EMPLEADO%TYPE,
    p_cargo IN EMPLEADOS.CARGO%TYPE,
    p_fecha_contratacion IN EMPLEADOS.FECHA_CONTRATACION%TYPE,
    p_salario IN EMPLEADOS.SALARIO%TYPE)
IS
BEGIN
    UPDATE EMPLEADOS
    SET 
        NOMBRE_EMPLEADO = p_nombre_empleado,
        APELLIDO_EMPLEADO = p_apellido_empleado,
        CARGO = p_cargo,
        FECHA_CONTRATACION = p_fecha_contratacion,
        SALARIO = p_salario
    WHERE ID_EMPLEADO = p_id_empleado;
    DBMS_OUTPUT.PUT_LINE('DATOS ACTUALIZADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el empleado con el ID: ' || p_id_empleado);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_UPDATE_EMPLEADO;



CREATE OR REPLACE PROCEDURE SP_DELETE_EMPLEADO(p_id_empleado IN EMPLEADOS.ID_EMPLEADO%TYPE)
IS
BEGIN
    DELETE FROM EMPLEADOS
    WHERE ID_EMPLEADO = p_id_empleado;
    DBMS_OUTPUT.PUT_LINE('DATOS ELIMINADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el empleado con el ID: ' || p_id_empleado);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_DELETE_EMPLEADO;











CREATE OR REPLACE PROCEDURE SP_INSERT_PROVEEDOR(
    p_id_proveedor IN PROVEEDORES.ID_PROVEEDOR%TYPE,
    p_nombre_proveedor IN PROVEEDORES.NOMBRE_PROVEEDOR%TYPE,
    p_direccion IN PROVEEDORES.DIRECCION%TYPE,
    p_correo_proveedor IN PROVEEDORES.CORREO_PROVEEDOR%TYPE)
IS
BEGIN
    INSERT INTO PROVEEDORES(ID_PROVEEDOR, NOMBRE_PROVEEDOR, DIRECCION, CORREO_PROVEEDOR)
    VALUES (p_id_proveedor, p_nombre_proveedor, p_direccion, p_correo_proveedor);
    DBMS_OUTPUT.PUT_LINE('DATOS INSERTADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el proveedor con el ID: ' || p_id_proveedor);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_INSERT_PROVEEDOR;



CREATE OR REPLACE PROCEDURE SP_SELECT_PROVEEDOR(p_id_proveedor IN PROVEEDORES.ID_PROVEEDOR%TYPE)
IS
    v_nombre_proveedor PROVEEDORES.NOMBRE_PROVEEDOR%TYPE;
    v_direccion PROVEEDORES.DIRECCION%TYPE;
    v_correo_proveedor PROVEEDORES.CORREO_PROVEEDOR%TYPE;
BEGIN
    SELECT NOMBRE_PROVEEDOR, DIRECCION, CORREO_PROVEEDOR
    INTO v_nombre_proveedor, v_direccion, v_correo_proveedor
    FROM PROVEEDORES
    WHERE ID_PROVEEDOR = p_id_proveedor;

    DBMS_OUTPUT.PUT_LINE('Nombre Proveedor: ' || v_nombre_proveedor || ', Direcci�n: ' || v_direccion 
                         || ', Correo Proveedor: ' || v_correo_proveedor);
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el proveedor con el ID: ' || p_id_proveedor);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_SELECT_PROVEEDOR;



CREATE OR REPLACE PROCEDURE SP_UPDATE_PROVEEDOR(
    p_id_proveedor IN PROVEEDORES.ID_PROVEEDOR%TYPE,
    p_nombre_proveedor IN PROVEEDORES.NOMBRE_PROVEEDOR%TYPE,
    p_direccion IN PROVEEDORES.DIRECCION%TYPE,
    p_correo_proveedor IN PROVEEDORES.CORREO_PROVEEDOR%TYPE)
IS
BEGIN
    UPDATE PROVEEDORES
    SET 
        NOMBRE_PROVEEDOR = p_nombre_proveedor,
        DIRECCION = p_direccion,
        CORREO_PROVEEDOR = p_correo_proveedor
    WHERE ID_PROVEEDOR = p_id_proveedor;
    DBMS_OUTPUT.PUT_LINE('DATOS ACTUALIZADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el proveedor con el ID: ' || p_id_proveedor);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_UPDATE_PROVEEDOR;



CREATE OR REPLACE PROCEDURE SP_DELETE_PROVEEDOR(p_id_proveedor IN PROVEEDORES.ID_PROVEEDOR%TYPE)
IS
BEGIN
    DELETE FROM PROVEEDORES
    WHERE ID_PROVEEDOR = p_id_proveedor;
    DBMS_OUTPUT.PUT_LINE('DATOS ELIMINADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el proveedor con el ID: ' || p_id_proveedor);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_DELETE_PROVEEDOR;









CREATE OR REPLACE PROCEDURE SP_INSERT_PRODUCTO(
    p_id_producto IN PRODUCTOS.ID_PRODUCTO%TYPE,
    p_id_proveedor IN PRODUCTOS.ID_PROVEEDOR%TYPE,
    p_cantidad IN PRODUCTOS.CANTIDAD%TYPE,
    p_descripcion IN PRODUCTOS.DESCRIPCION%TYPE,
    p_precio_producto IN PRODUCTOS.PRECIO_PRODUCTO%TYPE)
IS
BEGIN
    INSERT INTO PRODUCTOS(ID_PRODUCTO, ID_PROVEEDOR, CANTIDAD, DESCRIPCION, PRECIO_PRODUCTO)
    VALUES (p_id_producto, p_id_proveedor, p_cantidad, p_descripcion, p_precio_producto);
    DBMS_OUTPUT.PUT_LINE('DATOS INSERTADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el producto con el ID: ' || p_id_producto);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_INSERT_PRODUCTO;



CREATE OR REPLACE PROCEDURE SP_SELECT_PRODUCTO(p_id_producto IN PRODUCTOS.ID_PRODUCTO%TYPE)
IS
    v_id_proveedor PRODUCTOS.ID_PROVEEDOR%TYPE;
    v_cantidad PRODUCTOS.CANTIDAD%TYPE;
    v_descripcion PRODUCTOS.DESCRIPCION%TYPE;
    v_precio_producto PRODUCTOS.PRECIO_PRODUCTO%TYPE;
BEGIN
    SELECT ID_PROVEEDOR, CANTIDAD, DESCRIPCION, PRECIO_PRODUCTO
    INTO v_id_proveedor, v_cantidad, v_descripcion, v_precio_producto
    FROM PRODUCTOS
    WHERE ID_PRODUCTO = p_id_producto;

    DBMS_OUTPUT.PUT_LINE('ID Proveedor: ' || v_id_proveedor || ', Cantidad: ' || v_cantidad 
                         || ', Descripci�n: ' || v_descripcion || ', Precio Producto: ' || v_precio_producto);
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el producto con el ID: ' || p_id_producto);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_SELECT_PRODUCTO;



CREATE OR REPLACE PROCEDURE SP_UPDATE_PRODUCTO(
    p_id_producto IN PRODUCTOS.ID_PRODUCTO%TYPE,
    p_id_proveedor IN PRODUCTOS.ID_PROVEEDOR%TYPE,
    p_cantidad IN PRODUCTOS.CANTIDAD%TYPE,
    p_descripcion IN PRODUCTOS.DESCRIPCION%TYPE,
    p_precio_producto IN PRODUCTOS.PRECIO_PRODUCTO%TYPE)
IS
BEGIN
    UPDATE PRODUCTOS
    SET 
        ID_PROVEEDOR = p_id_proveedor,
        CANTIDAD = p_cantidad,
        DESCRIPCION = p_descripcion,
        PRECIO_PRODUCTO = p_precio_producto
    WHERE ID_PRODUCTO = p_id_producto;
    DBMS_OUTPUT.PUT_LINE('DATOS ACTUALIZADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el producto con el ID: ' || p_id_producto);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_UPDATE_PRODUCTO;



CREATE OR REPLACE PROCEDURE SP_DELETE_PRODUCTO(p_id_producto IN PRODUCTOS.ID_PRODUCTO%TYPE)
IS
BEGIN
    DELETE FROM PRODUCTOS
    WHERE ID_PRODUCTO = p_id_producto;
    DBMS_OUTPUT.PUT_LINE('DATOS ELIMINADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el producto con el ID: ' || p_id_producto);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_DELETE_PRODUCTO;







CREATE OR REPLACE PROCEDURE SP_INSERT_TRATAMIENTO(
    p_id_tratamiento IN TRATAMIENTOS.ID_TRATAMIENTO%TYPE,
    p_id_producto IN TRATAMIENTOS.ID_PRODUCTO%TYPE,
    p_descripcion IN TRATAMIENTOS.DESCRIPCION%TYPE,
    p_duracion_estimada IN TRATAMIENTOS.DURACION_ESTIMADA%TYPE,
    p_precio_tratamiento IN TRATAMIENTOS.PRECIO_TRATAMIENTO%TYPE)
IS
BEGIN
    INSERT INTO TRATAMIENTOS(ID_TRATAMIENTO, ID_PRODUCTO, DESCRIPCION, DURACION_ESTIMADA, PRECIO_TRATAMIENTO)
    VALUES (p_id_tratamiento, p_id_producto, p_descripcion, p_duracion_estimada, p_precio_tratamiento);
    DBMS_OUTPUT.PUT_LINE('DATOS INSERTADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el tratamiento con el ID: ' || p_id_tratamiento);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_INSERT_TRATAMIENTO;



CREATE OR REPLACE PROCEDURE SP_SELECT_TRATAMIENTO(p_id_tratamiento IN TRATAMIENTOS.ID_TRATAMIENTO%TYPE)
IS
    v_id_producto TRATAMIENTOS.ID_PRODUCTO%TYPE;
    v_descripcion TRATAMIENTOS.DESCRIPCION%TYPE;
    v_duracion_estimada TRATAMIENTOS.DURACION_ESTIMADA%TYPE;
    v_precio_tratamiento TRATAMIENTOS.PRECIO_TRATAMIENTO%TYPE;
BEGIN
    SELECT ID_PRODUCTO, DESCRIPCION, DURACION_ESTIMADA, PRECIO_TRATAMIENTO
    INTO v_id_producto, v_descripcion, v_duracion_estimada, v_precio_tratamiento
    FROM TRATAMIENTOS
    WHERE ID_TRATAMIENTO = p_id_tratamiento;

    DBMS_OUTPUT.PUT_LINE('ID Producto: ' || v_id_producto || ', Descripci�n: ' || v_descripcion 
                         || ', Duraci�n Estimada: ' || v_duracion_estimada || ', Precio Tratamiento: ' || v_precio_tratamiento);
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el tratamiento con el ID: ' || p_id_tratamiento);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_SELECT_TRATAMIENTO;




CREATE OR REPLACE PROCEDURE SP_UPDATE_TRATAMIENTO(
    p_id_tratamiento IN TRATAMIENTOS.ID_TRATAMIENTO%TYPE,
    p_id_producto IN TRATAMIENTOS.ID_PRODUCTO%TYPE,
    p_descripcion IN TRATAMIENTOS.DESCRIPCION%TYPE,
    p_duracion_estimada IN TRATAMIENTOS.DURACION_ESTIMADA%TYPE,
    p_precio_tratamiento IN TRATAMIENTOS.PRECIO_TRATAMIENTO%TYPE)
IS
BEGIN
    UPDATE TRATAMIENTOS
    SET 
        ID_PRODUCTO = p_id_producto,
        DESCRIPCION = p_descripcion,
        DURACION_ESTIMADA = p_duracion_estimada,
        PRECIO_TRATAMIENTO = p_precio_tratamiento
    WHERE ID_TRATAMIENTO = p_id_tratamiento;
    DBMS_OUTPUT.PUT_LINE('DATOS ACTUALIZADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el tratamiento con el ID: ' || p_id_tratamiento);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_UPDATE_TRATAMIENTO;




CREATE OR REPLACE PROCEDURE SP_DELETE_TRATAMIENTO(p_id_tratamiento IN TRATAMIENTOS.ID_TRATAMIENTO%TYPE)
IS
BEGIN
    DELETE FROM TRATAMIENTOS
    WHERE ID_TRATAMIENTO = p_id_tratamiento;
    DBMS_OUTPUT.PUT_LINE('DATOS ELIMINADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� el tratamiento con el ID: ' || p_id_tratamiento);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_DELETE_TRATAMIENTO;









CREATE OR REPLACE PROCEDURE SP_INSERT_CITA(
    p_id_cita IN CITAS.ID_CITA%TYPE,
    p_id_paciente IN CITAS.ID_PACIENTE%TYPE,
    p_id_empleado IN CITAS.ID_EMPLEADO%TYPE,
    p_id_tratamiento IN CITAS.ID_TRATAMIENTO%TYPE,
    p_fecha_cita IN CITAS.FECHA_CITA%TYPE,
    p_hora_cita IN CITAS.HORA_CITA%TYPE,
    p_observaciones IN CITAS.OBSERVACIONES%TYPE)
IS
BEGIN
    INSERT INTO CITAS(ID_CITA, ID_PACIENTE, ID_EMPLEADO, ID_TRATAMIENTO, FECHA_CITA, HORA_CITA, OBSERVACIONES)
    VALUES (p_id_cita, p_id_paciente, p_id_empleado, p_id_tratamiento, p_fecha_cita, p_hora_cita, p_observaciones);
    DBMS_OUTPUT.PUT_LINE('DATOS INSERTADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� la cita con el ID: ' || p_id_cita);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_INSERT_CITA;



CREATE OR REPLACE PROCEDURE SP_SELECT_CITA(p_id_cita IN CITAS.ID_CITA%TYPE)
IS
    v_id_paciente CITAS.ID_PACIENTE%TYPE;
    v_id_empleado CITAS.ID_EMPLEADO%TYPE;
    v_id_tratamiento CITAS.ID_TRATAMIENTO%TYPE;
    v_fecha_cita CITAS.FECHA_CITA%TYPE;
    v_hora_cita CITAS.HORA_CITA%TYPE;
    v_observaciones CITAS.OBSERVACIONES%TYPE;
BEGIN
    SELECT ID_PACIENTE, ID_EMPLEADO, ID_TRATAMIENTO, FECHA_CITA, HORA_CITA, OBSERVACIONES
    INTO v_id_paciente, v_id_empleado, v_id_tratamiento, v_fecha_cita, v_hora_cita, v_observaciones
    FROM CITAS
    WHERE ID_CITA = p_id_cita;

    DBMS_OUTPUT.PUT_LINE('ID Paciente: ' || v_id_paciente || ', ID Empleado: ' || v_id_empleado || ', ID Tratamiento: ' || v_id_tratamiento 
                         || ', Fecha Cita: ' || TO_CHAR(v_fecha_cita, 'DD-MON-YYYY') || ', Hora Cita: ' || TO_CHAR(v_hora_cita, 'HH24:MI:SS') 
                         || ', Observaciones: ' || v_observaciones);
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� la cita con el ID: ' || p_id_cita);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_SELECT_CITA;



CREATE OR REPLACE PROCEDURE SP_UPDATE_CITA(
    p_id_cita IN CITAS.ID_CITA%TYPE,
    p_id_paciente IN CITAS.ID_PACIENTE%TYPE,
    p_id_empleado IN CITAS.ID_EMPLEADO%TYPE,
    p_id_tratamiento IN CITAS.ID_TRATAMIENTO%TYPE,
    p_fecha_cita IN CITAS.FECHA_CITA%TYPE,
    p_hora_cita IN CITAS.HORA_CITA%TYPE,
    p_observaciones IN CITAS.OBSERVACIONES%TYPE)
IS
BEGIN
    UPDATE CITAS
    SET 
        ID_PACIENTE = p_id_paciente,
        ID_EMPLEADO = p_id_empleado,
        ID_TRATAMIENTO = p_id_tratamiento,
        FECHA_CITA = p_fecha_cita,
        HORA_CITA = p_hora_cita,
        OBSERVACIONES = p_observaciones
    WHERE ID_CITA = p_id_cita;
    DBMS_OUTPUT.PUT_LINE('DATOS ACTUALIZADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� la cita con el ID: ' || p_id_cita);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_UPDATE_CITA;



CREATE OR REPLACE PROCEDURE SP_DELETE_CITA(p_id_cita IN CITAS.ID_CITA%TYPE)
IS
BEGIN
    DELETE FROM CITAS
    WHERE ID_CITA = p_id_cita;
    DBMS_OUTPUT.PUT_LINE('DATOS ELIMINADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� la cita con el ID: ' || p_id_cita);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_DELETE_CITA;









CREATE OR REPLACE PROCEDURE SP_INSERT_FACTURA(
    p_id_factura IN FACTURAS.ID_FACTURA%TYPE,
    p_id_cita IN FACTURAS.ID_CITA%TYPE,
    p_fecha_emision IN FACTURAS.FECHA_EMISION%TYPE,
    p_subtotal IN FACTURAS.SUBTOTAL%TYPE,
    p_impuestos IN FACTURAS.IMPUESTOS%TYPE,
    p_total IN FACTURAS.TOTAL%TYPE)
IS
BEGIN
    INSERT INTO FACTURAS(ID_FACTURA, ID_CITA, FECHA_EMISION, SUBTOTAL, IMPUESTOS, TOTAL)
    VALUES (p_id_factura, p_id_cita, p_fecha_emision, p_subtotal, p_impuestos, p_total);
    DBMS_OUTPUT.PUT_LINE('DATOS INSERTADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� la factura con el ID: ' || p_id_factura);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_INSERT_FACTURA;



CREATE OR REPLACE PROCEDURE SP_SELECT_FACTURA(p_id_factura IN FACTURAS.ID_FACTURA%TYPE)
IS
    v_id_cita FACTURAS.ID_CITA%TYPE;
    v_fecha_emision FACTURAS.FECHA_EMISION%TYPE;
    v_subtotal FACTURAS.SUBTOTAL%TYPE;
    v_impuestos FACTURAS.IMPUESTOS%TYPE;
    v_total FACTURAS.TOTAL%TYPE;
BEGIN
    SELECT ID_CITA, FECHA_EMISION, SUBTOTAL, IMPUESTOS, TOTAL
    INTO v_id_cita, v_fecha_emision, v_subtotal, v_impuestos, v_total
    FROM FACTURAS
    WHERE ID_FACTURA = p_id_factura;

    DBMS_OUTPUT.PUT_LINE('ID Cita: ' || v_id_cita || ', Fecha de emisi�n: ' || TO_CHAR(v_fecha_emision, 'DD-MON-YYYY') 
                         || ', Subtotal: ' || v_subtotal || ', Impuestos: ' || v_impuestos || ', Total: ' || v_total);
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� la factura con el ID: ' || p_id_factura);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_SELECT_FACTURA;



CREATE OR REPLACE PROCEDURE SP_UPDATE_FACTURA(
    p_id_factura IN FACTURAS.ID_FACTURA%TYPE,
    p_id_cita IN FACTURAS.ID_CITA%TYPE,
    p_fecha_emision IN FACTURAS.FECHA_EMISION%TYPE,
    p_subtotal IN FACTURAS.SUBTOTAL%TYPE,
    p_impuestos IN FACTURAS.IMPUESTOS%TYPE,
    p_total IN FACTURAS.TOTAL%TYPE)
IS
BEGIN
    UPDATE FACTURAS
    SET 
        ID_CITA = p_id_cita,
        FECHA_EMISION = p_fecha_emision,
        SUBTOTAL = p_subtotal,
        IMPUESTOS = p_impuestos,
        TOTAL = p_total
    WHERE ID_FACTURA = p_id_factura;
    DBMS_OUTPUT.PUT_LINE('DATOS ACTUALIZADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� la factura con el ID: ' || p_id_factura);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_UPDATE_FACTURA;



CREATE OR REPLACE PROCEDURE SP_DELETE_FACTURA(p_id_factura IN FACTURAS.ID_FACTURA%TYPE)
IS
BEGIN
    DELETE FROM FACTURAS
    WHERE ID_FACTURA = p_id_factura;
    DBMS_OUTPUT.PUT_LINE('DATOS ELIMINADOS CORRECTAMENTE');
EXCEPTION 
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontr� la factura con el ID: ' || p_id_factura);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error inesperado: ' || SQLERRM);
        RAISE;
END SP_DELETE_FACTURA;


--10 Vistas



--15 Funciones



--10 Paquetes



--5 Triggers



--15 Cursores



