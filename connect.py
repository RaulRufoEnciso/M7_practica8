import psycopg2

# Conexión a base de datos
conn = psycopg2.connect(user='postgres',
                        password='admin',
                        host='127.0.0.1',
                        port='5432',
                        database='Personas')

# Usar curspr
cur = conn.cursor()

# Crear sentecia sql
sql = 'SELECT * FROM personas'

# Query SQL
cur.execute(sql)

# Mostrar resultados
resultados = cur.fetchall()
print(resultados)

# Cerrar conexion
# conn.close()