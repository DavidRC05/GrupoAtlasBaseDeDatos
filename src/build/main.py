import random
import os
import cx_Oracle
from datetime import datetime

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font, ttk, Label, messagebox

# Para caminos relativos
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#--- ACCIONES PARA BOTONES ---#

def esconderElementosExcepto(elementos_a_mantener):
    
    navbar = ["BackGround", "BtnActualizar", "BtnBuscar", "BtnAgregar", "BtnBorrar", "BtnLogo"]
    
    for name, (element_type, element) in tkinter_elements.items():
        if name not in elementos_a_mantener and name not in navbar: 
            if element_type != "image":
                element.place_forget()        
            else:
                canvas.itemconfigure(element, state="hidden")
        
def mostrarElementos(elementos_a_mostrar):
    for name, (element_type, element) in tkinter_elements.items():
        if name in elementos_a_mostrar:
            if element_type == "button" or element_type == "combo" or element_type == "treeview":
                x, y = element.initial_coords  
                element.place(x=x, y=y)  
            elif element_type != "image":
                x, y, width, height = element.initial_coords  
                element.place(x=x, y=y, width=width, height=height)  
            else:
                canvas.itemconfigure(element, state="normal")
                
def mostrarBuscarAccion():
    entry_values = {}
    
    selected_value = tkinter_elements["DropdownMenu"][1].get()  # Get selected value from the combobox   
    for entry_name in table_entries[selected_value]:
        entry = tkinter_elements[entry_name][1]+","
        value = entry.get()

        if not value:
            value = None

        entry_values[entry_name] = value
    
def showCurrentEntries():
    
       selected_value = tkinter_elements["DropdownMenu"][1].get()  # Get selected value from the combobox
       if selected_value in table_queries:
           
         mostrarElementos(table_entries[selected_value] + ['Texto' + selected_value])
       
#===============================================#
# AQUI EMPIEZA LAS ACCIONES DE LOS BOTONES CRUD # 
#===============================================#

#--------- Funciones para simplificar ----------#

def randomID():
    return random.randint(1, 5)
    
# Agarra el valor de un entrie normal
def get_entry_value(entry_name):
    return tkinter_elements[entry_name][1].get().strip()

# Funcion para crear un nuevo ID
def generateID(id_type):
    connection = None
    cursor = None
    new_id = 0
    try:
        connection = cx_Oracle.connect(
            user='C##ADMINISTRADOR',
            password='administrador123',
            dsn='localhost:1521/ORCL',
            mode=cx_Oracle.SYSDBA,
            encoding='UTF-8'
        ) 
        cursor = connection.cursor()
        # Este codigo agarra el mayor employee_id y le suma 1, para que siempre los employees id sean mayor al anterior
        #-----------------------------------#
        selected_value = tkinter_elements["DropdownMenu"][1].get()  
        cursor.execute(f"SELECT MAX({id_type}) FROM C##ADMINISTRADOR.{selected_value}")
        max_employee_id = cursor.fetchone()[0]
        if max_employee_id is None:
          new_id = 1
        new_id = max_employee_id + 1
        #-----------------------------------#
    except cx_Oracle.Error as error:
        print("Error:", error)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        return new_id

#===============================================#
#                    BUSCAR                     # 
#===============================================#

def accionBuscar():
        
        selected_value = tkinter_elements["DropdownMenu"][1].get()  
        query =  table_queries[selected_value][0] + " where "
        conditions = []
        vacio = True
       
        if selected_value == "Pacientes":

            #--------------------#
            paciente_nombre = get_entry_value("PacienteEntry_Nombre")
            paciente_apellido1 = get_entry_value("PacienteEntry_Apellido1")
            paciente_apellido2 = get_entry_value("PacienteEntry_Apellido2")
            paciente_correo = get_entry_value("PacienteEntry_Correo")
            paciente_genero = get_entry_value("PacienteEntry_Genero")
            paciente_año = get_entry_value("PacienteEntry_Año")
            paciente_mes = get_entry_value("PacienteEntry_Mes")
            paciente_dia = get_entry_value("PacienteEntry_Dia")
            fecha = paciente_año + "-" + paciente_mes + "-" + paciente_dia + " 00:00:00"
            paciente_descripcion = tkinter_elements["PacienteEntry_Descripcion"][1].get("1.0", "end-1c").strip() 
            
            #---------------------#
        
            if paciente_nombre:
                conditions.append(f"NOMBRE = '{paciente_nombre}'")
                vacio = False
            if paciente_apellido1 and paciente_apellido2:
                conditions.append(f"APELLIDO = '{paciente_apellido1 + ' ' +paciente_apellido2}'")
                vacio = False
            else:
                if paciente_apellido1:
                    conditions.append(f"APELLIDO = '{paciente_apellido1}'")
                    vacio = False
                if paciente_apellido2:
                    conditions.append(f"APELLIDO = '{paciente_apellido2}'")
                    vacio = False               
            if paciente_correo:
                conditions.append(f"CORREO_ELECTRONICO = '{paciente_correo}'")
                vacio = False
            if paciente_genero:
                conditions.append(f"GENERO = '{paciente_genero}'")
                vacio = False
            if paciente_año and paciente_mes and paciente_dia:
                conditions.append(f"FECHA_NACIMIENTO = TO_DATE('{fecha}', 'YYYY-MM-DD HH24:MI:SS')")
                vacio = False   
            if paciente_descripcion:
                conditions.append(f"DIRECCION = '{paciente_descripcion}'")
                vacio = False
           
            
        if selected_value == "Empleados":
            
            #--------------------#
            empleado_nombre = get_entry_value("EmpleadoEntry_Nombre")
            empleado_apellido1 = get_entry_value("EmpleadoEntry_Apellido1")
            empleado_apellido2 = get_entry_value("EmpleadoEntry_Apellido2")
            empleado_cargo = get_entry_value("EmpleadoEntry_Cargo")
            empleado_año = get_entry_value("EmpleadoEntry_Año")
            empleado_mes = get_entry_value("EmpleadoEntry_Mes")
            empleado_dia = get_entry_value("EmpleadoEntry_Dia")
            empleado_salario = get_entry_value("EmpleadoEntry_Salario")
            fecha = empleado_año + "-" + empleado_mes + "-" + empleado_dia + " 00:00:00"
             #---------------------#
            
            if empleado_nombre:
                conditions.append(f"NOMBRE_EMPLEADO = '{empleado_nombre}'")
                vacio = False
            if empleado_apellido1 and empleado_apellido2:
                conditions.append(f"APELLIDO_EMPLEADO = '{empleado_apellido1 + ' ' +empleado_apellido2}'")
                vacio = False
            else:
                if empleado_apellido1:
                    conditions.append(f"APELLIDO_EMPLEADO = '{empleado_apellido1}'")
                    vacio = False
                if empleado_apellido2:
                    conditions.append(f"APELLIDO_EMPLEADO = '{empleado_apellido2}'")
                    vacio = False 
            if empleado_cargo:
                conditions.append(f"CARGO = '{empleado_cargo}'")
                vacio = False
            if empleado_año and empleado_mes and empleado_dia:
                conditions.append(f"FECHA_CONTRATACION = TO_DATE('{fecha}', 'YYYY-MM-DD HH24:MI:SS')")
                vacio = False   
            if empleado_salario:
                conditions.append(f"SALARIO = '{empleado_salario}'")
                vacio = False
       
        if selected_value == "Proveedores":
            
            #--------------------#
            proveedor_nombre = get_entry_value("ProveedorEntry_Nombre")
            proveedor_direccion = get_entry_value("ProveedorEntry_Direccion") 
            proveedor_email = get_entry_value("ProveedorEntry_Email")
           #---------------------#
            
            if proveedor_nombre:
                conditions.append(f"NOMBRE_PROVEEDOR = '{proveedor_nombre}'")
                vacio = False
            if proveedor_direccion:
                conditions.append(f"DIRECCION = '{proveedor_direccion}'")
                vacio = False
            if proveedor_email:
                conditions.append(f"CORREO_PROVEEDOR = '{proveedor_email}'")
                vacio = False
       
        if selected_value == "Productos":
            
            #--------------------#
            producto_cantidad = get_entry_value("ProductoEntry_Cantidad")
            producto_nombre = get_entry_value("ProductoEntry_Nombre")
            producto_precio = get_entry_value("ProductoEntry_Precio")
           #---------------------#
            
            if producto_cantidad:
                conditions.append(f"CANTIDAD = '{producto_cantidad}'")
                vacio = False
            if producto_nombre:
                conditions.append(f"DESCRIPCION = '{producto_nombre}'")
                vacio = False
            if producto_precio:
                conditions.append(f"PRECIO_PRODUCTO = '{producto_precio}'")
                vacio = False    
                
            # esto es para agregar en un futuro (osea ya)
            #conditions.append(f"ID_PROVEEDOR = 1")
       
        if selected_value == "Tratamientos":
            
            #--------------------#
            tratamiento_descripcion = tkinter_elements["TratamientoEntry_Descripcion"][1].get("1.0", "end-1c").strip()
            tratamiento_duracion = get_entry_value("TratamientoEntry_DuracionEstimado")
            tratamiento_precio = get_entry_value("TratamientoEntry_Precio")
           #---------------------#
            
            if tratamiento_descripcion:
                conditions.append(f"DESCRIPCION = '{tratamiento_descripcion}'")
                vacio = False
            if tratamiento_duracion:
                conditions.append(f"DURACION_ESTIMADA = '{tratamiento_duracion}'")
                vacio = False
            if tratamiento_precio:
                conditions.append(f"PRECIO_TRATAMIENTO = '{tratamiento_precio}'")
                vacio = False    
       
       
        if selected_value == "Citas":
            #--------------------#
            cita_paciente = get_entry_value("CitaEntry_Paciente")
            cita_empleado = get_entry_value("CitaEntry_Empleado")
            cita_tratamiento = get_entry_value("CitaEntry_Tratamiento")
            cita_año = get_entry_value("CitaEntry_Año")
            cita_mes = get_entry_value("CitaEntry_Mes")
            cita_dia = get_entry_value("CitaEntry_Dia")
            fecha = cita_año + "-" + cita_mes + "-" + cita_dia + " 00:00:00"
            cita_hora = get_entry_value("CitaEntry_Hora")
            hora = "2023-08-01 " + cita_hora + ":00:00"
            cita_observacion = tkinter_elements["CitaEntry_Observaciones"][1].get("1.0", "end-1c").strip() #This is a text area
            #---------------------#
        
            if cita_paciente:
                conditions.append(f"ID_PACIENTE = '{cita_paciente}'")
                vacio = False
            if cita_empleado:
                conditions.append(f"ID_EMPLEADO = '{cita_empleado}'")
                vacio = False
            if cita_tratamiento:
                conditions.append(f"ID_TRATAMIENTO = '{cita_tratamiento}'")
                vacio = False
            if cita_año and cita_mes and cita_dia:
                print(fecha)
                conditions.append(f"FECHA_CITA = TO_DATE('{fecha}', 'YYYY-MM-DD HH24:MI:SS')")
                vacio = False   
            if cita_hora:
                print(cita_hora)
                conditions.append(f"HORA_CITA = TO_DATE('{hora}', 'YYYY-MM-DD HH24:MI:SS')")
                vacio = False    
            if cita_observacion:
                conditions.append(f"OBSERVACIONES = '{cita_observacion}'")
                vacio = False
       
       
        if selected_value == "Facturas":
            #--------------------#
            factura_paciente = get_entry_value("FacturaEntry_Cita")
            factura_año = get_entry_value("FacturaEntry_Año")
            factura_mes = get_entry_value("FacturaEntry_Mes")
            factura_dia = get_entry_value("FacturaEntry_Dia")
            fecha = factura_año + "-" + factura_mes + "-" + factura_dia + " 00:00:00"
            factura_empleado = get_entry_value("FacturaEntry_Subtotal")
            factura_tratamiento = get_entry_value("FacturaEntry_Impuestos")
            factura_total = get_entry_value("FacturaEntry_Total")
            #---------------------#
        
            if factura_paciente:
                conditions.append(f"ID_CITA = '{factura_paciente}'")
                vacio = False
            if factura_año and factura_mes and factura_dia:
                conditions.append(f"FECHA_EMISION = TO_DATE('{fecha}', 'YYYY-MM-DD HH24:MI:SS')")
                vacio = False
            if factura_empleado:
                conditions.append(f"SUBTOTAL = '{factura_empleado}'")
                vacio = False   
            if factura_tratamiento:
                conditions.append(f"IMPUESTOS = '{factura_tratamiento}'")
                vacio = False
            if factura_total:
                conditions.append(f"TOTAL = '{factura_total}'")
                vacio = False
        
        #============================================================#
          
        # Ejecutar query 
        
        if conditions:
                query += " AND ".join(conditions)  
        if not vacio:
                updateTreeView(tkinter_elements["Tabla"][1], table_queries[selected_value][1], query)
        else:
            updateTreeView(tkinter_elements["Tabla"][1], table_queries[selected_value][1], table_queries[selected_value][0])
        

#===============================================#
#                   AGREGAR                     # 
#===============================================#

def accionAgregar():
    
    selected_value = tkinter_elements["DropdownMenu"][1].get()  
    if selected_value == "Pacientes":
                        
        #--------------------#
        paciente_nombre = get_entry_value("PacienteEntry_Nombre")
        paciente_apellido1 = get_entry_value("PacienteEntry_Apellido1")
        paciente_apellido2 = get_entry_value("PacienteEntry_Apellido2")
        paciente_correo = get_entry_value("PacienteEntry_Correo")
        paciente_genero = get_entry_value("PacienteEntry_Genero")
        paciente_año = get_entry_value("PacienteEntry_Año")
        paciente_mes = get_entry_value("PacienteEntry_Mes")
        paciente_dia = get_entry_value("PacienteEntry_Dia")
        fecha = paciente_año + "-" + paciente_mes + "-" + paciente_dia 
        paciente_descripcion = tkinter_elements["PacienteEntry_Descripcion"][1].get("1.0", "end-1c").strip() 
        #--------------------#
        if paciente_apellido1 and paciente_apellido2:
                apellido = paciente_apellido1 + ' ' +paciente_apellido2            
        else:
                if paciente_apellido1:
                    apellido = paciente_apellido1
                if paciente_apellido2:
                    apellido = paciente_apellido2
                    
                    
        if paciente_nombre and paciente_apellido1 and paciente_correo and paciente_genero:
            query = f"""
            INSERT INTO 
            C##ADMINISTRADOR.PACIENTES (ID_PACIENTE, NOMBRE, APELLIDO, FECHA_NACIMIENTO, GENERO, DIRECCION, TELEFONO, CORREO_ELECTRONICO)
            VALUES ({generateID('ID_PACIENTE')}, '{paciente_nombre}', '{apellido}', TO_DATE('{fecha}','YYYY-MM-DD'), '{paciente_genero}', '{paciente_descripcion}', '8802-9999', '{paciente_correo}')"""    
            queryAndCommit(query)
      
    
    if selected_value == "Empleados":
        
        #--------------------#
        empleado_nombre = get_entry_value("EmpleadoEntry_Nombre")
        empleado_apellido1 = get_entry_value("EmpleadoEntry_Apellido1")
        empleado_apellido2 = get_entry_value("EmpleadoEntry_Apellido2")
        empleado_cargo = get_entry_value("EmpleadoEntry_Cargo")
        empleado_año = get_entry_value("EmpleadoEntry_Año")
        empleado_mes = get_entry_value("EmpleadoEntry_Mes")
        empleado_dia = get_entry_value("EmpleadoEntry_Dia")
        fecha = empleado_año + "-" + empleado_mes + "-" + empleado_dia
        empleado_salario = get_entry_value("EmpleadoEntry_Salario")
        #---------------------#
        
        if empleado_apellido1 and empleado_apellido2:
                apellido = empleado_apellido1 + ' ' +empleado_apellido2            
        else:
                if empleado_apellido1:
                    apellido = empleado_apellido1
                if empleado_apellido2:
                    apellido = empleado_apellido2
                    
                    
        if empleado_nombre and empleado_apellido1 and empleado_cargo and empleado_salario:
            query = f"""
            INSERT INTO 
            C##ADMINISTRADOR.EMPLEADOS (ID_EMPLEADO, NOMBRE_EMPLEADO, APELLIDO_EMPLEADO, CARGO, FECHA_CONTRATACION, SALARIO)
            VALUES ({generateID('ID_EMPLEADO')}, '{empleado_nombre}', '{apellido}', '{empleado_cargo}', TO_DATE('{fecha}','YYYY-MM-DD'), {empleado_salario})
            """    
            queryAndCommit(query)
       
    if selected_value == "Proveedores":
        
        #--------------------#
        proveedor_nombre = get_entry_value("ProveedorEntry_Nombre")
        proveedor_direccion = get_entry_value("ProveedorEntry_Direccion") 
        proveedor_email = get_entry_value("ProveedorEntry_Email")
        #---------------------#
        if proveedor_nombre and proveedor_direccion and proveedor_email:
            query = f"""
            INSERT INTO 
            C##ADMINISTRADOR.PROVEEDORES (ID_PROVEEDOR, NOMBRE_PROVEEDOR, DIRECCION, CORREO_PROVEEDOR)
            VALUES ({generateID('ID_PROVEEDOR')}, '{proveedor_nombre}', '{proveedor_direccion}', '{proveedor_email}')  
            """    
            queryAndCommit(query)
       
    if selected_value == "Productos":
        
        #--------------------#
        producto_cantidad = get_entry_value("ProductoEntry_Cantidad")
        producto_nombre = get_entry_value("ProductoEntry_Nombre")
        producto_precio = get_entry_value("ProductoEntry_Precio")
        #---------------------#
       
        if producto_cantidad and producto_nombre and producto_precio:
            query = f"""
            INSERT INTO 
            C##ADMINISTRADOR.PRODUCTOS (ID_PRODUCTO, ID_PROVEEDOR, CANTIDAD, DESCRIPCION, PRECIO_PRODUCTO)
            VALUES ({generateID('ID_PRODUCTO')}, {randomID()}, {producto_cantidad}, '{producto_nombre}', {producto_precio})
            """    
            queryAndCommit(query)
                   
    if selected_value == "Tratamientos":
        
        #--------------------#
        tratamiento_descripcion = tkinter_elements["TratamientoEntry_Descripcion"][1].get("1.0", "end-1c").strip()
        tratamiento_duracion = get_entry_value("TratamientoEntry_DuracionEstimado")
        tratamiento_precio = get_entry_value("TratamientoEntry_Precio")
        #---------------------#
        
        if tratamiento_descripcion and tratamiento_duracion and tratamiento_precio:
            query = f"""
            INSERT INTO 
            C##ADMINISTRADOR.TRATAMIENTOS (ID_TRATAMIENTO, ID_PRODUCTO, DESCRIPCION, DURACION_ESTIMADA, PRECIO_TRATAMIENTO)
            VALUES ({generateID('ID_TRATAMIENTO')}, {randomID()}, '{tratamiento_descripcion}', {tratamiento_duracion}, {tratamiento_precio})
            """    
            queryAndCommit(query)
            
       
    if selected_value == "Citas":
        
        #--------------------#
        cita_paciente = get_entry_value("CitaEntry_Paciente")
        cita_empleado = get_entry_value("CitaEntry_Empleado")
        cita_tratamiento = get_entry_value("CitaEntry_Tratamiento")
        cita_año = get_entry_value("CitaEntry_Año")
        cita_mes = get_entry_value("CitaEntry_Mes")
        cita_dia = get_entry_value("CitaEntry_Dia")
        fecha = cita_año + "-" + cita_mes + "-" + cita_dia
        cita_hora = get_entry_value("CitaEntry_Hora")
        hora = cita_hora + ":00:00"
        cita_observacion = tkinter_elements["CitaEntry_Observaciones"][1].get("1.0", "end-1c").strip() #This is a text area
        #---------------------#
        
        if cita_paciente and cita_empleado and cita_tratamiento and cita_observacion:
            query = f"""
            INSERT INTO 
            C##ADMINISTRADOR.CITAS (ID_CITA, ID_PACIENTE, ID_EMPLEADO, ID_TRATAMIENTO, FECHA_CITA, HORA_CITA, OBSERVACIONES)
            VALUES ({generateID('ID_CITA')}, {cita_paciente}, {cita_empleado}, {cita_tratamiento}, TO_DATE('{fecha}', 'YYYY-MM-DD'), TO_TIMESTAMP('{hora}', 'HH24:MI:SS'), '{cita_observacion}')
            """    
            queryAndCommit(query)
     
       
    if selected_value == "Facturas":
        
        #--------------------#
        factura_cita = get_entry_value("FacturaEntry_Cita")
        factura_año = get_entry_value("FacturaEntry_Año")
        factura_mes = get_entry_value("FacturaEntry_Mes")
        factura_dia = get_entry_value("FacturaEntry_Dia")
        fecha = factura_año + "-" + factura_mes + "-" + factura_dia
        factura_subtotal = get_entry_value("FacturaEntry_Subtotal")
        factura_impuestos = get_entry_value("FacturaEntry_Impuestos")
        factura_total = get_entry_value("FacturaEntry_Total")
        #---------------------#
        
        if factura_cita and factura_subtotal and factura_impuestos and factura_total:
            query = f"""
            INSERT INTO 
            C##ADMINISTRADOR.FACTURAS (ID_FACTURA, ID_CITA, FECHA_EMISION, SUBTOTAL, IMPUESTOS, TOTAL)
            VALUES ({generateID('ID_FACTURA')}, {factura_cita}, TO_DATE('{fecha}', 'YYYY-MM-DD'), {factura_subtotal}, {factura_impuestos}, {factura_total})
            """    
            queryAndCommit(query)

#===============================================#
#                   MODIFICAR                   # 
#===============================================#

def startModifyQuery(valorYcolumna):
    selected_value = tkinter_elements["DropdownMenu"][1].get()
    query = f"UPDATE C##ADMINISTRADOR.{selected_value} SET" 
    longitud = 0
    n_columna = 0
    # medir cuantos ahi, "para ajustar la coma"
    for valor in valorYcolumna:
      if valor[0]:
         longitud += 1
         
    # adjuntar string al query
    for valor in valorYcolumna:
        if valor[0]:
            if valor[2] == 0:
                query += f" {valor[1]} = '{valor[0]}'"
            else:
                query += f" {valor[1]} = {valor[0]}"
            n_columna += 1
            if not(n_columna >= longitud):
                query += ","
    return query

def agregarComaFecha(query, string):
    selected_value = tkinter_elements["DropdownMenu"][1].get()
    if query == f"UPDATE C##ADMINISTRADOR.{selected_value} SET": 
        new_string = string
    else:
        new_string = ","+string
    return new_string
    
def accionModificar():
      # Get selected value from the combobox
    
    selected_value = tkinter_elements["DropdownMenu"][1].get()
    
    if selected_value == "Pacientes":
        
        apellido1 = get_entry_value("PacienteEntry_Apellido1")
        apellido2 = get_entry_value("PacienteEntry_Apellido2")
        
        if apellido1 and apellido2:
                apellido = apellido1 + ' ' +apellido2
        else:
                if apellido1:
                    apellido = apellido1
                if apellido2:
                    apellido = apellido2
                    
        valorYcolumna = [
            (get_entry_value("PacienteEntry_Nombre"), "NOMBRE", 0),
            (apellido, "APELLIDO", 0),
            (get_entry_value("PacienteEntry_Correo"), "CORREO_ELECTRONICO", 0),
            (get_entry_value("PacienteEntry_Genero"), "GENERO", 0),
            (tkinter_elements["PacienteEntry_Descripcion"][1].get("1.0", "end-1c").strip(), "DIRECCION", 0)
        ]
        #--------------------#
        paciente_año = get_entry_value("PacienteEntry_Año")
        paciente_mes = get_entry_value("PacienteEntry_Mes")
        paciente_dia = get_entry_value("PacienteEntry_Dia")
        fecha = paciente_año + "-" + paciente_mes + "-" + paciente_dia 
        #--------------------#
        
        # se agregan todos los datos no vacios al query
        query = startModifyQuery(valorYcolumna)
        
        # este va a aparte porque es diferente a los otros datos
        if paciente_año and paciente_mes and paciente_dia:
                query += agregarComaFecha(query,f" FECHA_NACIMIENTO = TO_DATE('{fecha}', 'YYYY-MM-DD')")
        
        # agregar el where
        if get_entry_value("generalIdEntry"):      
            query += f" WHERE ID_PACIENTE = {get_entry_value('generalIdEntry')}"
            queryAndCommit(query)
    
    if selected_value == "Empleados":
            
            apellido1 = get_entry_value("EmpleadoEntry_Apellido1")
            apellido2 = get_entry_value("EmpleadoEntry_Apellido2")
        
            if apellido1 and apellido2:
                apellido = apellido1 + ' ' +apellido2
            else:
                if apellido1:
                    apellido = apellido1
                if apellido2:
                    apellido = apellido2
                    
            valorYcolumna = [
            (get_entry_value("EmpleadoEntry_Nombre"), "NOMBRE_EMPLEADO", 0),
            (apellido, "APELLIDO_EMPLEADO", 0),
            (get_entry_value("EmpleadoEntry_Cargo"), "CARGO", 0),
            (get_entry_value("EmpleadoEntry_Salario"), "SALARIO", 1)
            ]
            
            empleado_año = get_entry_value("EmpleadoEntry_Año")
            empleado_mes = get_entry_value("EmpleadoEntry_Mes")
            empleado_dia = get_entry_value("EmpleadoEntry_Dia")
            fecha = empleado_año + "-" + empleado_mes + "-" + empleado_dia 
            
            # se agregan todos los datos no vacios al query
            query = startModifyQuery(valorYcolumna)
            
            # este va a aparte porque es diferente a los otros datos
            if empleado_año and empleado_mes and empleado_dia:
                query += agregarComaFecha(query,f" FECHA_CONTRATACION = TO_DATE('{fecha}', 'YYYY-MM-DD')")
        
            if get_entry_value("generalIdEntry"):      
                query += f" WHERE ID_EMPLEADO = {get_entry_value('generalIdEntry')}"
                queryAndCommit(query)
            
    if selected_value == "Proveedores":
        
            valorYcolumna = [
            (get_entry_value("ProveedorEntry_Nombre"), "NOMBRE_PROVEEDOR", 0),
            (get_entry_value("ProveedorEntry_Direccion"), "DIRECCION", 0),
            (get_entry_value("ProveedorEntry_Email"), "CORREO_PROVEEDOR", 0),
            ]
            
            # se agregan todos los datos no vacios al query
            query = startModifyQuery(valorYcolumna)
        
            if get_entry_value("generalIdEntry"):      
                query += f" WHERE ID_PROVEEDOR = {get_entry_value('generalIdEntry')}"
                queryAndCommit(query)
       
    if selected_value == "Productos":
        
        valorYcolumna = [
        (get_entry_value("ProductoEntry_Cantidad"), "CANTIDAD", 1),
        (get_entry_value("ProductoEntry_Nombre"), "DESCRIPCION", 0),
        (get_entry_value("ProductoEntry_Precio"), "PRECIO_PRODUCTO", 1),
        ]
        
        # se agregan todos los datos no vacios al query
        query = startModifyQuery(valorYcolumna)
        
        if get_entry_value("generalIdEntry"):      
                query += f" WHERE ID_PRODUCTO = {get_entry_value('generalIdEntry')}"
                queryAndCommit(query)
    
    if selected_value == "Tratamientos":
        
        valorYcolumna = [
        (tkinter_elements["TratamientoEntry_Descripcion"][1].get("1.0", "end-1c").strip(), "DESCRIPCION", 0),
        (get_entry_value("TratamientoEntry_DuracionEstimado"), "DURACION_ESTIMADA", 1),
        (get_entry_value("TratamientoEntry_Precio"), "PRECIO_TRATAMIENTO", 1),
         ]
        
        # se agregan todos los datos no vacios al query
        query = startModifyQuery(valorYcolumna)
        
        if get_entry_value("generalIdEntry"):      
            query += f" WHERE ID_TRATAMIENTO = {get_entry_value('generalIdEntry')}"
            queryAndCommit(query)
    
    if selected_value == "Citas":
        
        valorYcolumna = [
            (get_entry_value("CitaEntry_Paciente"), "ID_PACIENTE", 1),
            (get_entry_value("CitaEntry_Empleado"), "ID_EMPLEADO", 1),
            (get_entry_value("CitaEntry_Tratamiento"), "ID_TRATAMIENTO", 1),
            (tkinter_elements["CitaEntry_Observaciones"][1].get("1.0", "end-1c").strip(), "OBSERVACIONES", 0)
        ]
        
        cita_año = get_entry_value("CitaEntry_Año")
        cita_mes = get_entry_value("CitaEntry_Mes")
        cita_dia = get_entry_value("CitaEntry_Dia")
        fecha = cita_año + "-" + cita_mes + "-" + cita_dia 
        
        cita_hora = get_entry_value("CitaEntry_Hora")
        hora = cita_hora + ":00:00"
       
        # se agregan todos los datos no vacios al query
        query = startModifyQuery(valorYcolumna)
        
        # este va a aparte porque es diferente a los otros datos
        if cita_año and cita_mes and cita_dia:
            query += agregarComaFecha(query,f" FECHA_CITA = TO_DATE('{fecha}', 'YYYY-MM-DD')")
        if cita_hora:
            query += agregarComaFecha(query,f" HORA_CITA = TO_TIMESTAMP('{hora}', 'HH24:MI:SS')")
        
        if get_entry_value("generalIdEntry"):      
            query += f" WHERE ID_CITA = {get_entry_value('generalIdEntry')}"
            queryAndCommit(query)
    
    if selected_value == "Facturas":
        
        valorYcolumna = [
            (get_entry_value("FacturaEntry_Cita"), "ID_CITA", 1),
            (get_entry_value("FacturaEntry_Subtotal"), "SUBTOTAL", 1),
            (get_entry_value("FacturaEntry_Impuestos"), "IMPUESTOS", 1),
            (get_entry_value("FacturaEntry_Total"), "TOTAL", 1)
        ]
        
        factura_año = get_entry_value("FacturaEntry_Año")
        factura_mes = get_entry_value("FacturaEntry_Mes")
        factura_dia = get_entry_value("FacturaEntry_Dia")
        fecha = factura_año + "-" + factura_mes + "-" + factura_dia
        
        # se agregan todos los datos no vacios al query
        query = startModifyQuery(valorYcolumna)
        
        if factura_año and factura_mes and factura_dia:
            query += agregarComaFecha(query,f" FECHA_EMISION = TO_DATE('{fecha}', 'YYYY-MM-DD')")
            
        if get_entry_value("generalIdEntry"):      
            query += f" WHERE ID_FACTURA = {get_entry_value('generalIdEntry')}"
            queryAndCommit(query)

#===============================================#
#                    DELETE                     # 
#===============================================#

def confirmacionBorrado():
    result = messagebox.askyesno("Confirmation","¿Seguro que quieres borrar este dato?")
    if result:
        return True
    return False
        
def accionBorrar():
    
    selected_value = tkinter_elements["DropdownMenu"][1].get()
    query = f"DELETE FROM C##ADMINISTRADOR.{selected_value} WHERE " 
    
    if selected_value == "Pacientes":
        
        if get_entry_value("generalIdEntry"):      
            query += f"ID_PACIENTE = {get_entry_value('generalIdEntry')}"
            if confirmacionBorrado():
                queryAndCommit(query)
        
    if selected_value == "Empleados":
        
        if get_entry_value("generalIdEntry"):      
            query += f"ID_EMPLEADO = {get_entry_value('generalIdEntry')}"
            if confirmacionBorrado():
                queryAndCommit(query)
    
       
    if selected_value == "Proveedores":
        
        if get_entry_value("generalIdEntry"):      
            query += f"ID_PROVEEDOR = {get_entry_value('generalIdEntry')}"
            if confirmacionBorrado():
                queryAndCommit(query)
    
    if selected_value == "Productos":
        
        if get_entry_value("generalIdEntry"):      
            query += f"ID_PRODUCTO = {get_entry_value('generalIdEntry')}"
            if confirmacionBorrado():
                queryAndCommit(query)
    
    if selected_value == "Tratamientos":
        
        if get_entry_value("generalIdEntry"):      
            query += f" ID_TRATAMIENTO = {get_entry_value('generalIdEntry')}"
            if confirmacionBorrado():
                queryAndCommit(query)
    
    if selected_value == "Citas":
        
        if get_entry_value("generalIdEntry"):      
            query += f"ID_CITA = {get_entry_value('generalIdEntry')}"
            if confirmacionBorrado():
                queryAndCommit(query)
    
    if selected_value == "Facturas":
        
        if get_entry_value("generalIdEntry"):      
            query += f"ID_FACTURA = {get_entry_value('generalIdEntry')}"
            if confirmacionBorrado():
                queryAndCommit(query)
            
# ------ Execute Queries and update table ------------ #
    
def queryAndCommit(query):
    connection = None
    cursor = None
    try:
        # Replace these values with your database connection details
        connection = cx_Oracle.connect(
            user='C##ADMINISTRADOR',
            password='administrador123',
            dsn='localhost:1521/ORCL',
            mode=cx_Oracle.SYSDBA,
            encoding='UTF-8'
        ) 
        cursor = connection.cursor()
        print(query)    
        cursor.execute(query)  
        connection.commit()
        print("I executed and commited")
    except cx_Oracle.Error as error:
        print("Error:", error)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close() 
    
    selected_value = tkinter_elements["DropdownMenu"][1].get()        
    updateTreeView(tkinter_elements["Tabla"][1], table_queries[selected_value][1], table_queries[selected_value][0])
    
#--- FABRICAS DE WIDGETS ---#
      
def createImage( name, x, y ):
    image_image = PhotoImage(file=relative_to_assets(name+".png"))
    photo_images.append(image_image)
    image = canvas.create_image(x, y, image=image_image)
    tkinter_elements[name] = ("image", image) 

def createImgButton( name, x, y, on_click_action):
    image_image = PhotoImage(file=relative_to_assets(name+".png")) 
    photo_images.append(image_image)
    button = Button(canvas, image=image_image, borderwidth=0, highlightthickness=0,
                    command=on_click_action)
    button.initial_coords = (x, y)
    button.place(x=x, y=y)
    tkinter_elements[name] = ("button", button)

def createButton( name, text, w, h, size, x, y, on_click_action ):
    
    textFont = font.Font(family="Open Sans", size=size, weight="bold")
    
    button = Button(canvas, text=text, width=w, height=h, bg="#02403A",
                       fg="#F2F2F2", font=textFont , relief="raised", state="normal",
                       command=on_click_action)
    button.initial_coords = (x, y)
    button.place(x=x, y=y)
    tkinter_elements[name] = ("button", button) 

def createEntry ( name, x, y, width, height):
    entry = Entry( 
                  bd=0, 
                  bg="#FFFFFF",
                  fg="#000716", 
                  highlightthickness=0 )
    entry.place( x=x, y=y, width=width, height=height )
    entry.initial_coords = (x, y, width, height)
    tkinter_elements[name] = ("entry", entry)

def createTextArea( name, x, y, width, height):
    text_area = Text(
        bd=0, 
        bg="#FFFFFF", 
        fg="#000716", 
        highlightthickness=0
        )
    text_area.place( x=x, y=y, width=width, height=height )
    text_area.initial_coords = (x, y, width, height)
    tkinter_elements[name] = ("text_area", text_area)
          
def createComboBox( name, x, y, size, width ):
    
    tablas = ["Pacientes", "Empleados", "Proveedores", "Productos","Tratamientos","Citas","Facturas"]
    textFont = font.Font(family="Open Sans", size=size, weight="bold")
    
    combo = ttk.Combobox(
    canvas,
    state="readonly",
    values=tablas,
    width=width,
    font=textFont,
    foreground="#02403A",
    background="#F2F2F2", 
    justify="center",
    takefocus=True
    )
    
    combo.bind("<<ComboboxSelected>>", tablaFueElegida)
    combo.initial_coords = (x, y)
    combo.place(x=x, y=y)
    combo.set("Pacientes")
    tkinter_elements[name] = ("combo", combo)

def tablaFueElegida(event):
                   
    elementosAMostrar = []  
    selected_value = event.widget.get()
    
    if selected_value in table_queries:
            
        elementosAMostrar = table_entries[selected_value] + ['Texto' + selected_value]
        updateTreeView(tkinter_elements["Tabla"][1], table_queries[selected_value][1], table_queries[selected_value][0]) 
        
    esconderElementosExcepto(defaultCrud + CrudPageBtns + ["generalIDtext", "generalIdEntry"]), 
    mostrarElementos(elementosAMostrar)

def createTreeView(name, queryInfo, width, height, x, y):
    tree = ttk.Treeview(canvas, columns=queryInfo[1], show="headings", height=height)
    for col in queryInfo[1]:
        tree.heading(col, text=col)
        tree.column(col, width=int(width / len(queryInfo[1])), anchor="center")
   
    tree.place(x=x, y=y)
    tkinter_elements[name] = ("treeview", tree)
    
    updateTreeView(tree, queryInfo[1], queryInfo[0])
    tree.initial_coords = (x, y)

def updateTreeView(tree, columnas, query):
    selected_value = tkinter_elements["DropdownMenu"][1].get()
    id_type = table_queries[selected_value][2]
    connection = None
    cursor = None
    try:
        # Datos de la conexion a la base de datos
        connection = cx_Oracle.connect(
            user='C##ADMINISTRADOR',
            password='administrador123',
            dsn='localhost:1521/ORCL',
            mode=cx_Oracle.SYSDBA,
            encoding='UTF-8'
        ) 
        cursor = connection.cursor()
        query += f" order by {id_type} desc"
        print(query)
        cursor.execute(query) 
        print("query ejecutado")
        data = cursor.fetchall()
    except cx_Oracle.Error as error:
        print("Error:", error)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close() 
            
    # Quitar columnas existentes
    for col in tree['columns']:
        tree.heading(col, text="")

    # Poner nuevas columnas
    for idx, col in enumerate(columnas):
        tree.heading(idx, text=col)    
            
    # Borrar datos en la tabla
    for item in tree.get_children():
        tree.delete(item)
    
    # Poner nuevos datos
    if data is None:
        print("Query returned no data.")
        return
    
    for row in data:
        #print(row) #for debuggin
        tree.insert("", "end", values=row)

##############################
#--- UI WIDGET PRODUCTION ---#
##############################

def createNavbar():
    # --------------- BUTTONS --------------- #
    
    createImgButton("BtnLogo", 409, 16, 
                    lambda: ( 
                          esconderElementosExcepto([]), 
                          mostrarElementos( LandingPageBtns )
                          ))
    
    createImgButton("BtnAgregar", 69, 35, 
                    lambda: ( 
                          esconderElementosExcepto(AllEntries), 
                          mostrarElementos(defaultCrud + ["BtnAgregarTabla"] ),
                          showCurrentEntries()
                          ))
    
    createImgButton("BtnBuscar", 232, 35,  
                  lambda: ( 
                          esconderElementosExcepto(AllEntries), 
                          mostrarElementos(defaultCrud + ["BtnBuscarTabla"] ),
                          showCurrentEntries()
                          ))
    
    createImgButton("BtnActualizar", 616, 35, 
                    lambda: ( 
                          esconderElementosExcepto(AllEntries), 
                          mostrarElementos(defaultCrud + ["BtnActualizarTabla", "generalIDtext", "generalIdEntry"] ),
                          showCurrentEntries()
                          ))
    
    createImgButton("BtnBorrar", 778, 35,    
                  lambda: ( 
                          esconderElementosExcepto(AllEntries), 
                          mostrarElementos(defaultCrud + ["BtnBorrarTabla", "generalIDtext", "generalIdEntry"] ),
                          showCurrentEntries()
                          ))

    # --------------- IMAGENES -------------- #
    
    createImage("BackGround", 480, 300)
    
def createLandingPageBtns():   
    
    size = 18

    # --------------- BUTTONS --------------- #
    
    createButton( "BtnAgregarLP", "Agregar", 20, 1, size, 60, 250, 
                 lambda: ( 
                          esconderElementosExcepto([]), 
                          mostrarElementos(defaultCrud + ["BtnAgregarTabla"] ),
                          showCurrentEntries()
                          ))
    
    createButton( "BtnActualizarLP", "Actualizar", 20, 1, size, 60, 400,  
                 lambda: ( 
                          esconderElementosExcepto([]), 
                          mostrarElementos(defaultCrud + ["BtnActualizarTabla", "generalIDtext", "generalIdEntry"]   ),
                          showCurrentEntries()
                          ))
    
    createButton( "BtnBuscarLP", "Buscar", 20, 1, size, 565, 250, 
                 lambda: ( 
                          esconderElementosExcepto([]), 
                          mostrarElementos(defaultCrud + ["BtnBuscarTabla"] ),
                          showCurrentEntries()
                          ))
    
    createButton( "BtnBorrarLP", "Borrar", 20, 1, size, 565, 400, 
                 lambda: ( 
                          esconderElementosExcepto([]), 
                          mostrarElementos(defaultCrud + ["BtnBorrarTabla", "generalIDtext", "generalIdEntry"] ),
                          showCurrentEntries()
                          ))
    

def createCRUD ():
    
    #( name, x, y, size, width, on_select_action )
    createComboBox( "DropdownMenu", 280, 155, 12, 15 )
    # Create the table
    createTreeView("Tabla", QueryPacientes, 790, 14, 85, 266)
 
    
def createBtnsTabla ():
     
    size = 9
    
    # Agregar
    createButton( "BtnAgregarTabla", "Agregar", 20, 1, size, 520, 152, accionAgregar )
    # Actualizar
    createButton( "BtnActualizarTabla", "Actualizar", 20, 1, size, 520, 152, accionModificar )
    # Buscar
    createButton( "BtnBuscarTabla", "Buscar", 20, 1, size, 520, 152, accionBuscar )
    # Borrar
    createButton( "BtnBorrarTabla", "Borrar", 20, 1, size, 520, 152, accionBorrar )
    # Text and entrie ID for BUSCAR AND BORRAR
    
    #Turn this later into a function
    #----------------------------------------#
    generalIDtext = Label(canvas, text="ID:")
    generalIDtext.place(x=210, y=156)
    generalIDtext.initial_coords = (210, 156)
    tkinter_elements["generalIDtext"] = ("combo", generalIDtext)
    #----------------------------------------#
    createEntry ("generalIdEntry",232, 159, 43, 17)
    
#  --------- TEXTO Y ENTRIES DE CADA TABLA --------- #    

def createPacientesEntries ():
    
    # Textos pacientes
    createImage("TextoPacientes", 422, 202) 
    # Espacios a llenar pacientes
    createEntry ("PacienteEntry_Nombre",         65, 192, 85, 17)
    createEntry ("PacienteEntry_Genero",         65, 230, 85, 17)
    createEntry ("PacienteEntry_Apellido1",      229, 192, 85, 17) 
    createEntry ("PacienteEntry_Apellido2",      229, 230, 85, 17) 
    createEntry ("PacienteEntry_Año",            361, 230, 43, 17) 
    createEntry ("PacienteEntry_Mes",            447, 230, 43, 17)  
    createEntry ("PacienteEntry_Dia",            534, 230, 43, 17)
    createEntry ("PacienteEntry_Correo",         588, 230, 153, 17)
    createTextArea ("PacienteEntry_Descripcion", 757, 176, 165, 71)

def createEmpleadosEntries ():
    
    # Textos empleados
    createImage("TextoEmpleados", 330, 220)    
    # Espacios a llenar empleados
    createEntry ("EmpleadoEntry_Nombre",    65, 192, 85, 17)
    createEntry ("EmpleadoEntry_Cargo",     65, 230, 85, 17)
    createEntry ("EmpleadoEntry_Apellido1", 229, 192, 85, 17) 
    createEntry ("EmpleadoEntry_Apellido2", 229, 230, 85, 17)  
    createEntry ("EmpleadoEntry_Año",       361, 230, 43, 17) 
    createEntry ("EmpleadoEntry_Mes",       447, 230, 43, 17)  
    createEntry ("EmpleadoEntry_Dia",       534, 230, 43, 17)  
    createEntry ("EmpleadoEntry_Salario",   661, 211, 153, 17)
    
def createProveedoresEntries ():
    
    # Textos Proveedores
    createImage("TextoProveedores", 373, 230) 
    # Espacios a llenar Proveedores
    createEntry ("ProveedorEntry_Nombre",    162, 223, 161, 17)
    createEntry ("ProveedorEntry_Email",     378, 223, 170, 17)
    createEntry ("ProveedorEntry_Direccion", 652, 223, 161, 17) 
    
def createProductosEntries ():
    
    # Textos Productos
    createImage("TextoProductos", 403, 216) 
    # Espacios a llenar Productos
    createEntry ("ProductoEntry_Nombre",          152, 222, 132, 17)
    createEntry ("ProductoEntry_Cantidad",        370, 224, 88, 17)
    createEntry ("ProductoEntry_Precio",          529, 224, 87, 17) 
    createTextArea ("ProductoEntry_Descripcion",  637, 210, 228, 50)
 
def createTratamientosEntries ():
    # Textos tratamientos
    createImage("TextoTratamientos", 353.0, 215.0) 
    # Espacios a llenar tratamientos
    createEntry ("TratamientoEntry_DuracionEstimado", 258, 199, 162, 17)
    createEntry ("TratamientoEntry_Precio",           258, 227, 162, 17)
    createTextArea ("TratamientoEntry_Descripcion",   494, 205, 228, 50)
    
def createCitasEntries ():
    # Textos citas
    createImage("TextoCitas", 444, 217) 
    # Espacios a llenar citas
    createEntry ("CitaEntry_Paciente",         155, 198, 85, 17)
    createEntry ("CitaEntry_Empleado",         155, 232, 85, 17)
    createEntry ("CitaEntry_Año",              292, 198, 43, 17)
    createEntry ("CitaEntry_Mes",              385, 198, 43, 17)
    createEntry ("CitaEntry_Dia",              292, 232, 43, 17)
    createEntry ("CitaEntry_Hora",             385, 232, 43, 17)
    createEntry ("CitaEntry_Tratamiento",      598, 211, 85, 17)
    createTextArea ("CitaEntry_Observaciones", 708, 197, 145, 57)

def createFacturasEntries ():
    # Textos facturas
    createImage("TextoFacturas", 424, 226) 
    # Espacios a llenar facturas
    createEntry ("FacturaEntry_Cita",       135, 232, 85, 17)
    createEntry ("FacturaEntry_Año",           267, 232, 43, 17)
    createEntry ("FacturaEntry_Mes",           349, 232, 43, 17)
    createEntry ("FacturaEntry_Dia",           431, 232, 43, 17)
    createEntry ("FacturaEntry_Total",           576, 203, 85, 17)
    createEntry ("FacturaEntry_Impuestos",           576, 232, 85, 17)
    createEntry ("FacturaEntry_Subtotal",           752, 232, 85, 17)

#== GLOBAL CODE ==#

OUTPUT_PATH = Path(__file__).parent

IMAGE_DIRECTORY = os.getcwd() + "\\GrupoAtlasBaseDeDatos\\src\\build\\assets\\frame0"
ASSETS_PATH = OUTPUT_PATH / Path(IMAGE_DIRECTORY)

window = Tk()
window.geometry("960x600")
window.configure(bg = "#F9F9F9") 
    
canvas = Canvas(
    window,
    bg = "#F9F9F9",
    height = 600,
    width = 960,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
     
canvas.place(x = 0, y = 0)

# Elementos que quiero que aparezcan a la hora de cambiarse a cualquiera de los crud

defaultCrud = ["DropdownMenu","Tabla"]

# Arrays de todos los entries
first_time = True

entriesPacientes = [
    'PacienteEntry_Nombre', 
    'PacienteEntry_Correo', 
    'PacienteEntry_Genero', 
    'PacienteEntry_Apellido1',
    'PacienteEntry_Año', 
    'PacienteEntry_Mes', 
    'PacienteEntry_Dia',
    'PacienteEntry_Apellido2',
    'PacienteEntry_Descripcion'
]

entriesEmpleados = [
    'EmpleadoEntry_Nombre', 
    'EmpleadoEntry_Cargo',
    'EmpleadoEntry_Apellido1', 
    'EmpleadoEntry_Apellido2', 
    'EmpleadoEntry_Año', 
    'EmpleadoEntry_Mes', 
    'EmpleadoEntry_Dia', 
    'EmpleadoEntry_Salario'
]

entriesProveedores = [
    'ProveedorEntry_Nombre', 
    'ProveedorEntry_Email', 
    'ProveedorEntry_Direccion'
]

entriesProductos = [
    'ProductoEntry_Nombre', 
    'ProductoEntry_Cantidad', 
    'ProductoEntry_Precio', 
    'ProductoEntry_Descripcion'
]

entriesTratamientos = [
    "TratamientoEntry_DuracionEstimado", 
    "TratamientoEntry_Precio", 
    "TratamientoEntry_Descripcion"
]
    
entriesCitas = [
    "CitaEntry_Paciente",
    "CitaEntry_Empleado",
    "CitaEntry_Año",
    "CitaEntry_Mes",
    "CitaEntry_Dia",
    "CitaEntry_Hora",
    "CitaEntry_Tratamiento",
    "CitaEntry_Observaciones"
]

entriesFacturas = [
    "FacturaEntry_Cita",
    "FacturaEntry_Año",
    "FacturaEntry_Mes",
    "FacturaEntry_Dia",
    "FacturaEntry_Total",
    "FacturaEntry_Impuestos",
    "FacturaEntry_Subtotal"
]

AllEntrieTexts = [
    'TextoPacientes', 
    'TextoEmpleados', 
    'TextoProveedores', 
    'TextoProductos',
    'TextoCitas',
    'TextoFacturas'
]

AllEntries = entriesPacientes + entriesEmpleados + entriesProveedores + entriesProductos + entriesTratamientos + entriesCitas + entriesFacturas + AllEntrieTexts 

#Botones de landing page
LandingPageBtns = ["BtnAgregarLP","BtnBuscarLP","BtnActualizarLP","BtnBorrarLP"]

# Boton en crud de Agregar, buscar, Actualizar y borrar
CrudPageBtns = ["BtnAgregarTabla","BtnBuscarTabla","BtnActualizarTabla","BtnBorrarTabla"]

# En este diccionario se guarda la data de todos los elementos creados para poder ser elegidos en otras ocasiones
tkinter_elements = {}

# Array necesario a la hora de crear imagenes para la prevencion de que el garbage collector de python borre las imagenes
photo_images = [] 

# Queries y nombres de columnas

QueryPacientes = [
    "SELECT ID_PACIENTE, NOMBRE, APELLIDO, TO_CHAR(FECHA_NACIMIENTO, 'YYYY-MM-DD'), GENERO, DIRECCION, CORREO_ELECTRONICO FROM C##ADMINISTRADOR.PACIENTES",
        ["ID PACIENTE", "NOMBRE", "APELLIDO", "FECHA NACIMIENTO", "GENERO", "DESCRIPCION", "EMAIL"],
        "ID_PACIENTE"]
    
QueryEmpleados = [
        "SELECT ID_EMPLEADO, NOMBRE_EMPLEADO, APELLIDO_EMPLEADO, CARGO, TO_CHAR(FECHA_CONTRATACION, 'YYYY-MM-DD'), SALARIO FROM C##ADMINISTRADOR.EMPLEADOS",
        ["ID EMPLEADO", "NOMBRE", "APELLIDO", "CARGO", "FECHA CONTRATACION", "SALARIO"],
        "ID_EMPLEADO"]

QueryProveedores = [
        "SELECT ID_PROVEEDOR, NOMBRE_PROVEEDOR, DIRECCION, CORREO_PROVEEDOR FROM C##ADMINISTRADOR.PROVEEDORES",
        ["ID PROVEEDOR", "NOMBRE", "DIRECCION", "CORREO"],
        "ID_PROVEEDOR"]

QueryProductos = [
        "SELECT ID_PRODUCTO, CANTIDAD, DESCRIPCION, PRECIO_PRODUCTO FROM C##ADMINISTRADOR.PRODUCTOS",
        ["ID PRODUCTO", "CANTIDAD", "DESCRIPCION", "PRECIO"],
        "ID_PRODUCTO"]

QueryTratamientos = [
        "SELECT ID_TRATAMIENTO, DESCRIPCION, DURACION_ESTIMADA, PRECIO_TRATAMIENTO FROM C##ADMINISTRADOR.TRATAMIENTOS",
        ["ID TRATAMIENTO", "DESCRIPCION", "DURACION ESTIMADA", "PRECIO"],
        "ID_TRATAMIENTO"]
    
QueryCitas = [
        "SELECT ID_CITA, ID_PACIENTE, ID_EMPLEADO, ID_TRATAMIENTO, TO_CHAR(FECHA_CITA, 'YYYY-MM-DD'), TO_CHAR(HORA_CITA, 'HH24'), OBSERVACIONES FROM C##ADMINISTRADOR.CITAS",
        ["ID CITA", "ID PACIENTE", "ID EMPLEADO", "ID TRATAMIENTO", "FECHA CITA", "HORA CITA", "OBSERVACIONES"],
        "ID_CITA"]
          
QueryFacturas = [
        "SELECT ID_FACTURA, ID_CITA, TO_CHAR(FECHA_EMISION, 'YYYY-MM-DD'), SUBTOTAL, IMPUESTOS, TOTAL FROM C##ADMINISTRADOR.FACTURAS",
        ["ID FACTURA", "ID CITA", "FECHA EMISION", "SUBTOTAL", "IMPUESTOS", "TOTAL"],
        "ID_FACTURA"]

# diccionario de las tablas y sus datos
table_queries = {
    "Pacientes": QueryPacientes,
    "Empleados": QueryEmpleados,
    "Proveedores": QueryProveedores,
    "Productos": QueryProductos,
    "Tratamientos": QueryTratamientos,
    "Citas": QueryCitas,
    "Facturas": QueryFacturas,
}

#diccionario de cata tabla y sus entries respectivos
table_entries = {
    "Pacientes": entriesPacientes,
    "Empleados": entriesEmpleados,
    "Proveedores": entriesProveedores,
    "Productos": entriesProductos,
    "Tratamientos": entriesTratamientos,
    "Citas": entriesCitas,
    "Facturas": entriesFacturas,
}

#Crea todos los elementos
# Landing Page
createNavbar()
createLandingPageBtns() 

#Cruds
createCRUD()
createBtnsTabla()

#Creacion de los entries de cada tabla
createPacientesEntries()
createEmpleadosEntries()
createProveedoresEntries()
createProductosEntries()
createTratamientosEntries()
createCitasEntries()
createFacturasEntries()

#Esconde todos los elementos menos los del langing page
esconderElementosExcepto(LandingPageBtns) 

### TESTING TABLA ###

window.resizable(False, False)
window.mainloop()


