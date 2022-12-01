#importar modul psycopg2
import psycopg2

#connexio bbdd
conexion=psycopg2.connect(user='postgres', password='hola', host='127.0.0.1', port='5432', database='db_personas')

#cursor
cursor=conexion.cursor()

#sentencia sql
sql='SELECT * FROM personas'

#executar sentencia sql
cursor.execute(sql)

#guardar resultat a variable registro
registro=cursor.fetchall()

#output
print(registro)

#tancar connexio
cursor.close()
conexion.close()

