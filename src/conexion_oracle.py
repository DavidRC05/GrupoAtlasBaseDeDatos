import cx_Oracle

"""
Si tienes problemas con tu base de datos en Oracle:

SQLPLUS / AS SYSDBA
Abrir conexión => ALTER PLUGGABLE DATABASE ORCLPDB OPEN;
O preguntarle a Catalina

Este archivo es para hacer un testing inicial de conexion con la base de datos
"""

try:
    connection = cx_Oracle.connect(
        user='C##ADMINISTRADOR',
        password='administrador123',
        dsn='localhost:1521/ORCL',
        mode=cx_Oracle.SYSDBA,
        encoding='UTF-8'
    )
    print(connection.version)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM C##ADMINISTRADOR.PACIENTES")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    connection.close()  
    print("La conexión ha finalizado.")
