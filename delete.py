import connect

# Sentencia sql
sql ='DELETE FROM personas WHERE id_persona=%s'

# Solicitar datos al Usuario
id_persona = input('Ingrese el id del registro a eliminar: ')

# Usar metodo execute
connect.cur.execute(sql,id_persona)

# Guardar cambios
connect.conn.commit()

# Contador de registros eliminados
registro_eliminado = connect.cur.rowcount

# Mensaje al Usuario
print(f'Registro eliminado: {registro_eliminado}')

# Cerrar cursor
connect.cur.close()
connect.conn.close()

