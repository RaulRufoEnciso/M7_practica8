#importar modul psycopg2
import psycopg2

#connexio bbdd
conexion=psycopg2.connect(user='postgres', password='hola', host='127.0.0.1', port='5432', database='db_personas')

#cursor
cursor=conexion.cursor()

#SENTENCIA SQL
sql='INSERT INTO personas (nombre,apellido,edad) VALUES(%s,%s,%s)'

#solicitud noms
nombre=input('nom:')
apellido=input('cognom: ')
edad=input('edat: ')

#recolecció
datos=(nombre,apellido,edad)

cursor.execute(sql,datos)

conexion.commit()

registros=cursor.rowcount

print(f'registre insertat: {registros}')

cursor.close()
conexion.close()