import connect

# Crear sentencia sql
sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id_persona=%s'

id_persona = input('Ingrese el id de la persona que desea modificar: ')
nombre = input('Ingrese el nombre de la persona que desea modificar: ')
apellido = input('Ingrese el apellido de la persona que desea modificar: ')
edad = input('Ingrese el edad de la persona que desea modificar: ')

# Recogida de datos
datos = (nombre,apellido,edad,id_persona)

# Metodo execute
connect.cur.execute(sql,datos)

# Guardar modificaciones
connect.conn.commit()

# Contar el numero de modificaciones
actualizacion = connect.cur.rowcount

# Mostrar mensje al usuario
print(f'Registro accualizado: {actualizacion}')

# Cerrar cursor
connect.cur.close()
connect.conn.close()